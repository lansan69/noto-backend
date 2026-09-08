from app.features.auth.domain.repository.sign_user_in import UserValidationRepository

class SignUserIn:
    def __init__(self, validation_repository: UserValidationRepository):
        self.validation_repository = validation_repository

    async def execute(self, email: str, password: str):
        return await self.validation_repository.sign_in_jwt(email=email, password=password)