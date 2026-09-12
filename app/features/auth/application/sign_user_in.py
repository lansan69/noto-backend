from app.features.auth.domain.repository.sign_user_in import UserValidationRepository
from app.features.auth.domain.usecases.sign_user import SignUserIn

def create_sign_user_in_use_case(repository: UserValidationRepository) -> SignUserIn:
    return SignUserIn(repository)