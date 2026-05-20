from src.repositories.implementations.pg.user_repository import UserRepository
from src.services.interfaces.user_service import (
    IUserService
)



class UserService(IUserService):

    def __init__(self):

        self.user_repository = UserRepository()

    def get_by_login(self, login: str):

        return self.user_repository.get_by_login(
            login
        )

    def search_users(self, name: str):

        return self.user_repository.search_users(
            name
        )