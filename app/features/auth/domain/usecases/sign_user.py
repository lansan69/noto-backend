from app.features.auth.domain.repository.sign_user_in import UserValidationRepository
from app.features.auth.domain.exceptions import InvalidCredentialsError

class SignUserIn:
    def __init__(self, validationRepository: UserValidationRepository):
        self.validationRepository = validationRepository
    
    async def execute(self, email:str, password:str):
        try:
            return await self.validationRepository.sign_in_jwt(email=email, password=password)
        except InvalidCredentialsError:
            raise