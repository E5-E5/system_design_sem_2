from abc import ABC, abstractmethod

from src.model.user import User


class IAuthService(ABC):

    @abstractmethod
    def register(self, user: User):
        pass

    @abstractmethod
    def login(self, login: str, password: str):
        pass