from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from app.features.notes.domain.usecases.notes_usecases import TakeNotes
from app.features.notes.domain.exceptions import TranscriptError
from app.api.v1.notes.deps import create_note

transcript_router = APIRouter()  

@transcript_router.post("/notes/")
async def transcript(
    audio_file: UploadFile = File(..., description="Archivo de audio"),
    use_case: TakeNotes = Depends(create_note),
):
    try:
        return await use_case.execute(audio_bytes=await audio_file.read())
    except TranscriptError as e:
        raise HTTPException(422, f"Transcription failed: {e}")