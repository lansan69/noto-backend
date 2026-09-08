from abc import ABC, abstractmethod
from app.features.notes.domain.entities.notes_entities import NoteDraft
from app.features.notes.domain.entities.transcript import TranscriptResult

class NotesRepository(ABC): 
    
    @abstractmethod
    async def create_note(self, transcript: TranscriptResult) -> NoteDraft:
        pass
        