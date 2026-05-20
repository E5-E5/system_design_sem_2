from src.model.user import User
from src.services.interfaces.user_service import IUserService


class UserService(IUserService):

    def __init__(self):
        self.users = []

    def create_user(self, user: User):

        self.users.append(user)

        return user

    def get_by_login(self, login: str):

        for user in self.users:

            if user.login == login:
                return user

        return None

    def search_users(self, name: str):

        result = []

        for user in self.users:

            if (
                name.lower() in user.first_name.lower()
                or name.lower() in user.last_name.lower()
            ):
                result.append(user)

        return result