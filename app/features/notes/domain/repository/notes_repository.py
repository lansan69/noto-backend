from abc import ABC, abstractmethod
from app.features.notes.domain.entities.notes_entities import NoteDraft
from app.features.notes.domain.entities.transcript_entities import TranscriptResult

class NotesRepository(ABC): 
    
    @abstractmethod
    async def create_note(self, transcript: TranscriptResult, system_prompt:str) -> NoteDraft:
        pass
        