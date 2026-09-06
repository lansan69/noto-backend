from abc import ABC, abstractmethod

class UserValidationRepository(ABC):
    @abstractmethod
    async def sign_in_jwt(self, email: str, password: str) -> str:
        "Authenticates a user and returns access token"
        pass