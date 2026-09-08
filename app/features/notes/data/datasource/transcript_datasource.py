# features/notes/data/datasource/transcription_datasource.py
import asyncio
from assemblyai import Transcriber
from app.features.notes.data.models.transcript_models import TranscriptModel


class TranscriptionDatasource:
    def __init__(self, transcriber: Transcriber):
        self._transcriber = transcriber

    async def upload_file(self, audio_bytes: bytes) -> str:
        return await asyncio.to_thread(self._transcriber.upload_file, audio_bytes)

    async def create_transcript(self, audio_url: str) -> TranscriptModel:
        transcript = await asyncio.to_thread(self._transcriber.transcribe, audio_url)
        if transcript.status == "error":
            raise RuntimeError(transcript.error)
        return TranscriptModel.from_json(transcript.json_response)
    