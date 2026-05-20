from abc import ABC, abstractmethod


class IUserRepository(ABC):

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def get_by_login(self, login: str):
        pass

    @abstractmethod
    def search(self, name: str):
        pass