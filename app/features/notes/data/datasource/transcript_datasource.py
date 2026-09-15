# features/notes/data/datasource/transcription_datasource.py
import asyncio
import logging
from assemblyai import Transcriber
from openai import AsyncOpenAI
from app.features.notes.data.models.assemblyai_models import TranscriptResultModel
from app.features.notes.data.models.groq_models import (
    GroqTranscriptElement,
    GroqTranscriptResponse,
)
from assemblyai.prerecorded.v2 import TranscriptionConfig

# Initialize logger
logger = logging.getLogger(__name__)

class AssemblyAITranscriptionDatasource:
    def __init__(self, transcriber: Transcriber, transcription_config: TranscriptionConfig):
        self._transcriber = transcriber
        self._transcription_config = transcription_config

    async def upload_file_assemblyai(self, audio_bytes: bytes) -> str:
        return await asyncio.to_thread(self._transcriber.upload_file, audio_bytes)

    async def create_transcript_assemblyai(self, audio_bytes: bytes) -> TranscriptResultModel:
        logger.debug("Subiendo el archivo")
        audio_url = await self.upload_file_assemblyai(audio_bytes)
        
        logger.debug("Iniciando trasncripción")
        transcript = await asyncio.to_thread(self._transcriber.transcribe, audio_url, config=self._transcription_config)
        
        if transcript.status == "error":
            logger.exception(f"Error en la trasncripción: {transcript.error}")
            raise ValueError(f"Transcription API error: {transcript.error}")
        
        logger.debug("Transcripción exitosa")
        return TranscriptResultModel.model_validate(transcript.json_response)

class GroqTranscriptionDatasource:
    def __init__(self, client: AsyncOpenAI):
        self.client = client
    
    async def create_transcript_groq(self, audio_bytes: bytes) -> GroqTranscriptResponse:
        logger.debug("Subiendo el archivo y transcribiendo")
        transcription = await self.client.audio.transcriptions.create(
            file=("audio.m4a", audio_bytes, "audio/mp4"),
            model="whisper-large-v3-turbo",
            temperature=0,
            response_format="verbose_json",
        )
        logger.debug(f"Transcripción de Groq recibida: {transcription}")
        segments = transcription.segments or []
        utterances = [
            GroqTranscriptElement.model_validate(segment.model_dump())
            for segment in segments
        ]
        return GroqTranscriptResponse(utterances=utterances)