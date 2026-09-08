from app.features.notes.domain.repository.transcript import TranscriptRepository
from app.features.notes.domain.repository.notes_repository import NotesRepository
from app.features.notes.domain.entities.transcript import TranscriptResult
from app.features.notes.domain.entities.notes_entities import NoteDraft

class TakeNotes:
    def __init__(self, transcript_repository: TranscriptRepository, notes_repository: NotesRepository):
        self.transcript_repository = transcript_repository
        self.notes_repository = notes_repository
    
    async def transcribe(self, audio_bytes: bytes) -> TranscriptResult:
        audio_url = await self.transcript_repository.upload_file(audio_bytes=audio_bytes)
        return await self.transcript_repository.create_transcript(audio_url=audio_url)
    
    async def execute(self, audio_bytes: bytes) -> NoteDraft:
        transcript = await self.transcribe(audio_bytes=audio_bytes)
        return await self.notes_repository.create_note(transcript=transcript)