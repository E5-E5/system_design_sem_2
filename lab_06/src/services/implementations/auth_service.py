from src.model.user import User

from src.repositories.implementations.pg.user_repository import UserRepository
from src.services.interfaces.auth_service import IAuthService

from src.security.jwt_handler import create_access_token



class AuthService(IAuthService):

    def __init__(self):

        self.user_repository = UserRepository()

    def register(self, user: User):

        existing_user = self.user_repository.get_by_login(
            user.login
        )

        if existing_user is not None:
            return None

        user_id = self.user_repository.create(user)

        token = create_access_token(
            {
                "sub": user.login
            }
        )

        return {
            "user_id": user_id,
            "access_token": token,
            "token_type": "bearer"
        }

    def login(self, login: str, password: str):

        user = self.user_repository.get_by_login(login)

        if user is None:
            return None

        if user.password != password:
            return None

        token = create_access_token(
            {
                "sub": user.login
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }