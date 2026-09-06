from pydantic import BaseModel, Field


class SignInRequest(BaseModel):
    email: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)