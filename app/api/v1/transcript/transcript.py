from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from app.features.auth.domain.usecases.sign_user import SignUserIn
from app.features.auth.domain.exceptions import InvalidCredentialsError
from app.features.auth.application.sign_user_in import get_sign_user_in_use_case

router = APIRouter()

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class TranscriptResult(BaseModel):
    transcript: str = Field("", description="The transcribed text from the audio file")


class SignInRequest(BaseModel):
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)


# ---------------------------------------------------------------------------
# Transcription
# ---------------------------------------------------------------------------

# async def upload_file(audio_file: UploadFile) -> str:
#     contents = await audio_file.read()
#     upload_url = await asyncio.to_thread(transcriber.upload_file, contents)
#     return upload_url


# async def create_transcript(audio_file: UploadFile) -> TranscriptResult:
#     upload_url = await upload_file(audio_file)
#     transcript = await asyncio.to_thread(transcriber.transcribe, upload_url)

#     if transcript.status == "error":
#         raise RuntimeError(transcript.error)
#     return TranscriptResult(transcript=transcript.text)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@router.post("/signin/")
async def signin(
    body: SignInRequest,
    use_case: SignUserIn = Depends(get_sign_user_in_use_case),
):
    try:
        token = await use_case.execute(email=body.email, password=body.password)
        return {"access_token": token}
    except InvalidCredentialsError:
        raise HTTPException(401, "Invalid email or password")
    
# @router.post("/transcript/")
# async def transcript(
#     audio_file: Annotated[UploadFile, File()],
#     user_id: str = Depends(get_current_user_id),
# ) -> Any:
#     result = await create_transcript(audio_file)
#     # TODO: persist result as a note/block row scoped to user_id,
#     # relying on RLS policies to enforce ownership on write.
#     return result