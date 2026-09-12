# features/notes/data/datasource/transcription_datasource.py
import asyncio
import logging
from assemblyai import Transcriber
from app.features.notes.data.models.transcript_models import TranscriptResultModel
from assemblyai.prerecorded.v2 import TranscriptionConfig

# Initialize logger
logger = logging.getLogger(__name__)

class TranscriptionDatasource:
    def __init__(self, transcriber: Transcriber, transcription_config: TranscriptionConfig):
        self._transcriber = transcriber
        self._transcription_config = transcription_config

    async def upload_file(self, audio_bytes: bytes) -> str:
        return await asyncio.to_thread(self._transcriber.upload_file, audio_bytes)

    async def create_transcript(self, audio_bytes: bytes) -> TranscriptResultModel:
        logger.debug("Subiendo el archivo")
        audio_url = await self.upload_file(audio_bytes)
        
        logger.debug("Iniciando trasncripción")
        transcript = await asyncio.to_thread(self._transcriber.transcribe, audio_url, config=self._transcription_config)
        
        if transcript.status == "error":
            logger.exception(f"Error en la trasncripción: {transcript.error}")
            raise ValueError(f"Transcription API error: {transcript.error}")
        
        logger.debug("Transcripción exitosa")
        return TranscriptResultModel.model_validate(transcript.json_response)
