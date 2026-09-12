from app.features.notes.domain.repository.transcript import TranscriptRepository
from app.features.notes.domain.repository.notes_repository import NotesRepository
from app.features.notes.domain.entities.notes_entities import NoteDraft

class TakeNotes:
    def __init__(
        self,
        transcript_repository: TranscriptRepository,
        notes_repository: NotesRepository,
        system_prompt: str
        ):
        self.transcript_repository = transcript_repository
        self.notes_repository = notes_repository
        self.system_prompt = system_prompt
    
    async def execute(self, audio_bytes: bytes) -> NoteDraft:
        transcript = await self.transcript_repository.create_transcript(audio_bytes=audio_bytes)
        notes = await self.notes_repository.create_note(transcript=transcript, system_prompt=self.system_prompt)
        return notes