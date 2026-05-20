from abc import ABC, abstractmethod


class IHotelRepository(ABC):

    @abstractmethod
    def create(self, hotel):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_city(self, city: str):
        pass

    @abstractmethod
    def get_by_id(self, hotel_id: int):
        pass