from fastapi import Request
from app.features.notes.domain.usecases.notes_usecases import TakeNotes
from app.features.notes.data.datasource.transcript_datasource import AssemblyAITranscriptionDatasource
from app.features.notes.data.repository.transcript_repository_impl import AssemblyAITranscriptResultImpl
from app.features.notes.data.repository.alibaba_notes_repository_impl import AlibabaNotesRepositoryImpl
from app.features.notes.data.datasource.alibaba_notes_datasource import AlibabaNotesDatasource
from app.features.notes.application.take_notes import create_take_notes_use_case


async def create_note(request: Request) -> TakeNotes:
    transcriber = request.app.state.transcriber
    transcription_config = request.app.state.transcription_config

    alibaba_client = request.app.state.alibaba_client
    alibaba_models = request.app.state.alibaba_models

    transcript_datasource = AssemblyAITranscriptionDatasource(
        transcriber=transcriber,
        transcription_config=transcription_config
    )
    transcript_repository = AssemblyAITranscriptResultImpl(transcript_datasource)

    notes_datasource = AlibabaNotesDatasource(alibaba_models=alibaba_models, openai_client=alibaba_client)
    notes_repository = AlibabaNotesRepositoryImpl(notes_datasource)

    return create_take_notes_use_case(transcript_repository, notes_repository)
