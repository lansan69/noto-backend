from supabase import AsyncClient
from app.features.notes.data.models.assemblyai_models import TranscriptResultModel
from app.features.notes.data.models.notes_models import NotesModel

class SupabaseNotePersistenceDatasource:
    def __init__(self, supabase_client: AsyncClient):
        self.supabase_client = supabase_client
    
    async def save_transcript(self, transcript: TranscriptResultModel):
        # Pendiente
        pass 
    
    async def save_notes(self, notes: NotesModel ):
        # Pendiente
        pass