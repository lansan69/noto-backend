from fastapi import Request
from app.features.auth.data.datasource.sign_user_in_datasource import SupabaseUserValidationDatasource
from app.features.auth.data.repository.sign_user_in_impl import SupabaseUserValidationRepositoryImpl
from app.features.auth.application.sign_user_in import create_sign_user_in_use_case
from app.features.auth.domain.usecases.sign_user import SignUserIn


async def get_sign_user_in_use_case(request: Request) -> SignUserIn:
    supabase_admin = request.app.state.supabase_admin
    datasource = SupabaseUserValidationDatasource(supabase_admin)
    repository = SupabaseUserValidationRepositoryImpl(datasource)
    return create_sign_user_in_use_case(repository)
