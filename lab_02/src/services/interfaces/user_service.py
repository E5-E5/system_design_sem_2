from abc import ABC, abstractmethod

from src.model.user import User

class IUserService(ABC):

    @abstractmethod
    def create_user(self, user: User):
        pass

    @abstractmethod
    def get_by_login(self, login: str):
        pass

    @abstractmethod
    def search_users(self, name: str):
        pass