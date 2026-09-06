from fastapi import APIRouter, Depends, HTTPException
from app.features.auth.domain.usecases.sign_user import SignUserIn
from app.features.auth.domain.exceptions import InvalidCredentialsError
from app.features.auth.application.sign_user_in import get_sign_user_in_use_case
from app.api.schemas.signin.signin_schemas import SignInRequest

signin_router = APIRouter()  

@signin_router.post("/signin/")
async def signin(
    body: SignInRequest,
    use_case: SignUserIn = Depends(get_sign_user_in_use_case),
):
    try:
        token = await use_case.execute(email=body.email, password=body.password)
        return {"access_token": token}
    except InvalidCredentialsError:
        raise HTTPException(401, "Invalid email or password")