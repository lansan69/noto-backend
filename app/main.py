from contextlib import asynccontextmanager

from assemblyai import SpeechModel, Transcriber
from app.core.config import settings
from app.core.models import models
from fastapi import FastAPI
from jwt import PyJWKClient
from supabase import acreate_client
from app.api.v1.signin.signin import signin_router
from app.api.v1.notes.notes import transcript_router
from assemblyai.prerecorded.v2 import TranscriptionConfig
from openai import AsyncOpenAI
from app.core.logging import setup_logging

setup_logging()

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase_admin = await acreate_client(
        settings.SUPABASE_URL, settings.SUPABASE_API_KEY
    )
    app.state.jwks_client = PyJWKClient(settings.SUPABASE_JWS_URL)
    app.state.transcriber = Transcriber(api_key=settings.ASSEMBLYAI_API_KEY)
    app.state.transcription_config = TranscriptionConfig(
        speech_models=[
            *models.ASSEMBLYAI_MODELS
        ],
        format_text=True,
        punctuate=True,
        language_detection=True
    )
    app.state.alibaba_client = AsyncOpenAI(
        api_key = settings.ALIBABA_API_KEY,
        base_url = settings.ALIBABA_OPENAI_COMPATIBLE_ENDPOINT
    )
    app.state.alibaba_models = models.ALIBABA_MODELS
    app.state.groq_client = AsyncOpenAI(
        base_url=settings.GROQ_BASE_URL,
        api_key=settings.GROQ_API_KEY
    )
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(signin_router, prefix="")
app.include_router(transcript_router, prefix="")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}