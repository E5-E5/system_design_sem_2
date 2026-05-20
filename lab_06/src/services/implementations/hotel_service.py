from src.dto.dto import CreateHotelRequest
from src.repositories.implementations.mango.hotel_repository import HotelRepository_mango
from src.model.hotel import Hotel
from src.services.interfaces.hotel_service import (
    IHotelService
)
import json
from src.repositories.db.redis_database import RedisDatabase
from src.events.producer import EventProducer

class HotelService(IHotelService):

    def __init__(self):

        self.hotel_repository = HotelRepository_mango()
        self.redis = RedisDatabase().get_client()
        self.producer = EventProducer()

    def create_hotel(self, hotel: CreateHotelRequest):

        hotel_id = self.hotel_repository.create(
            hotel
        )
        self.redis.delete("hotels_all")
        self.redis.delete(f"hotels_city_{hotel.city.lower()}")

        self.producer.publish(
            "hotel.created",
            {
                "hotel_id": hotel_id,
                "city": hotel.city,
                "description": hotel.description
            }
        )

        return {
            "hotel_id": hotel_id
        }

    def get_hotels(self):

        cached_hotels = self.redis.get("hotels_all")

        if cached_hotels:

            return json.loads(cached_hotels)

        hotels = self.hotel_repository.get_all()

        result = []

        for hotel in hotels:

            result.append(
                {
                    "id": hotel.id,
                    "name": hotel.name,
                    "city": hotel.city,
                    "address": hotel.address,
                    "description": hotel.description
                }
            )

        self.redis.set(
            "hotels_all",
            json.dumps(result),
            ex=60
        )

        return result

    def event_publish(self, hotels):
        self.producer.publish("hotels.get", hotels)

    def get_hotels_by_city(self, city: str):

        cache_key = f"hotels_city_{city.lower()}"

        cached_hotels = self.redis.get(cache_key)

        if cached_hotels:
            self.event_publish(cached_hotels)
            return json.loads(cached_hotels)

        hotels = self.hotel_repository.get_by_city(city)

        result = []

        for hotel in hotels:
            # для постгреса
            # result.append(
            #     {
            #         "id": hotel.id,
            #         "name": hotel.name,
            #         "city": hotel.city,
            #         "address": hotel.address,
            #         "description": hotel.description
            #     }
            # )
            # монго
            result.append(
                {
                    "id": hotel["id"],
                    "name": hotel["name"],
                    "city": hotel["city"],
                    "address": hotel["address"],
                    "description": hotel["description"]
                }
    )

        self.redis.set(
            cache_key,
            json.dumps(result),
            ex=60
        )
        self.event_publish(hotels)
        return result