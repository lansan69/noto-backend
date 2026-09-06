# data/supabase/user_validation_impl.py
from supabase import AuthApiError

from app.features.auth.data.datasource.sign_user_in_data_source import UserValidationDatasource
from app.features.auth.domain.repository.sign_user_in import UserValidationRepository
from app.features.auth.domain.exceptions import InvalidCredentialsError

class UserValidationRepositoryImpl(UserValidationRepository):
    def __init__(self, datasource: UserValidationDatasource):
        self._datasource = datasource
    
    async def sign_in_jwt(self, email: str, password: str) -> str:
        try:
            access_token = await self._datasource.sign_in_with_password(email, password)
            return access_token
        except AuthApiError as e:
            raise InvalidCredentialsError("Invalid email or password") from e