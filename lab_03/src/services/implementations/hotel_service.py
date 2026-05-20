from src.model.hotel import Hotel

from src.repositories.implementations.hotel_repository import HotelRepository
from src.services.interfaces.hotel_service import (
    IHotelService
)



class HotelService(IHotelService):

    def __init__(self):

        self.hotel_repository = HotelRepository()

    def create_hotel(self, hotel: Hotel):

        hotel_id = self.hotel_repository.create(
            hotel
        )

        return {
            "hotel_id": hotel_id
        }

    def get_hotels(self):

        return self.hotel_repository.get_all()

    def get_hotels_by_city(self, city: str):

        return self.hotel_repository.get_by_city(
            city
        )