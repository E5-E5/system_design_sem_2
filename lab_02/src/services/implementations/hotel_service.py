from src.model.hotel import Hotel
from src.services.interfaces.hotel_service import IHotelService


class HotelService(IHotelService):

    def __init__(self):
        self.hotels = []

    def create_hotel(self, hotel: Hotel):

        self.hotels.append(hotel)

        return hotel

    def get_hotels(self):

        return self.hotels

    def get_hotels_by_city(self, city: str):

        result = []

        for hotel in self.hotels:

            if hotel.city.lower() == city.lower():
                result.append(hotel)

        return result