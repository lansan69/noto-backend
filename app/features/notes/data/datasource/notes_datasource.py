# data/datasources/user_validation_datasource.py
from app.features.notes.data.models.transcript_models import TranscriptModel
from openai import AsyncOpenAI

class NotesDatasource:
    def __init__(self, openai_client: AsyncOpenAI):
        self._openai_client = openai_client

    async def create_note(self, email: str, password: str) -> str:
        # Pendiente
        pass 