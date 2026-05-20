from abc import ABC, abstractmethod

from src.model.hotel import Hotel


class IHotelService(ABC):

    @abstractmethod
    def create_hotel(self, hotel: Hotel):
        pass

    @abstractmethod
    def get_hotels(self):
        pass

    @abstractmethod
    def get_hotels_by_city(self, city: str):
        pass