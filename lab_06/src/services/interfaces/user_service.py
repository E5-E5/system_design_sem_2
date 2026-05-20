from abc import ABC, abstractmethod

from src.model.user import User

class IUserService(ABC):

    @abstractmethod
    def get_by_login(self, login: str):
        pass
