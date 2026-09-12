from fastapi import Request
from app.features.auth.data.datasource.sign_user_in_data_source import UserValidationDatasource
from app.features.auth.data.repository.sign_user_in_impl import UserValidationRepositoryImpl
from app.features.auth.application.sign_user_in import create_sign_user_in_use_case
from app.features.auth.domain.usecases.sign_user import SignUserIn


async def get_sign_user_in_use_case(request: Request) -> SignUserIn:
    supabase_admin = request.app.state.supabase_admin
    datasource = UserValidationDatasource(supabase_admin)
    repository = UserValidationRepositoryImpl(datasource)
    return create_sign_user_in_use_case(repository)
