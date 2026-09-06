from contextlib import asynccontextmanager

from assemblyai import Transcriber
from app.core.config import settings
from fastapi import FastAPI
from jwt import PyJWKClient
from supabase import acreate_client
from app.api.v1.signin.signin import signin_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.supabase_admin = await acreate_client(
        settings.SUPABASE_URL, settings.SUPABASE_API_KEY
    )
    app.state.jwks_client = PyJWKClient(settings.SUPABASE_JWS_URL)
    app.state.transcriber = Transcriber(api_key=settings.ASSEMBLYAI_API_KEY)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(signin_router, prefix="")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}