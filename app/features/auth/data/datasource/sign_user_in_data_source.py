# data/datasources/user_validation_datasource.py
from supabase import AsyncClient

class UserValidationDatasource:
    def __init__(self, client: AsyncClient):
        self._client = client

    async def sign_in_with_password(self, email: str, password: str) -> str:
        response = await self._client.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
        return response.session.access_token