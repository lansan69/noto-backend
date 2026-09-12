from abc import ABC, abstractmethod
from app.features.notes.domain.entities.transcript_entities import TranscriptResult

class TranscriptRepository(ABC):
    
    @abstractmethod
    async def create_transcript(self, audio_bytes: bytes) -> TranscriptResult:
        pass
        