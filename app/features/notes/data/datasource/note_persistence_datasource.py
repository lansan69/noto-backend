from supabase import AsyncClient
from app.features.notes.data.models.transcript_models import TranscriptModel
from app.features.notes.data.models.notes_models import NoteDraftModel

class NotePersistentDatasource:
    def __init__(self, supabase_client: AsyncClient):
        self.supabase_client = supabase_client
    
    async def save_transcript(self, transcript: TranscriptModel):
        # Pendiente
        pass 
    
    async def save_notes(self, notes: NoteDraftModel ):
        # Pendiente
        pass