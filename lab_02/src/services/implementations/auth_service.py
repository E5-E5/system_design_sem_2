from src.model.user import User

from src.services.interfaces.auth_service import IAuthService

from src.security.jwt_handler import create_access_token


class AuthService(IAuthService):

    def __init__(self):
        self.users = []

    def register(self, user: User):

        for existing_user in self.users:

            if existing_user.login == user.login:
                return None

        self.users.append(user)

        token = create_access_token(
            {
                "sub": user.login
            }
        )

        return {
            "user": user,
            "access_token": token,
            "token_type": "bearer"
        }

    def login(self, login: str, password: str):

        for user in self.users:

            if (
                user.login == login
                and user.password == password
            ):

                token = create_access_token(
                    {
                        "sub": user.login
                    }
                )

                return {
                    "access_token": token,
                    "token_type": "bearer"
                }

        return None