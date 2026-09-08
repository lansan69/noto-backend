from abc import ABC, abstractmethod
from app.features.notes.domain.entities.transcript import TranscriptResult

class TranscriptRepository(ABC):
    
    @abstractmethod
    async def upload_file(self, audio_bytes: bytes) -> str:
        pass
    
    @abstractmethod
    async def create_transcript(self, audio_url: str) -> TranscriptResult:
        pass
        