from fastapi import Request
from app.features.notes.domain.usecases.notes_usecases import TakeNotes
from app.features.notes.data.datasource.transcript_datasource import TranscriptionDatasource
from app.features.notes.data.repository.transcript_repository_impl import TranscriptResultImpl
from app.features.notes.data.repository.notes_repository_impl import NotesRepositoryImpl
from app.features.notes.data.datasource.notes_datasource import NotesDatasource
from app.features.notes.application.take_notes import create_take_notes_use_case


async def create_note(request: Request) -> TakeNotes:
    transcriber = request.app.state.transcriber
    transcription_config = request.app.state.transcription_config
    supabase_admin = request.app.state.supabase_admin

    alibaba_client = request.app.state.alibaba_client
    alibaba_models = request.app.state.alibaba_models
    
    transcript_datasource = TranscriptionDatasource(transcriber, transcription_config)
    transcript_repository = TranscriptResultImpl(transcript_datasource)

    notes_datasource = NotesDatasource(alibaba_models=alibaba_models, openai_client=alibaba_client)
    notes_repository = NotesRepositoryImpl(notes_datasource)

    return create_take_notes_use_case(transcript_repository, notes_repository)
