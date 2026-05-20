from bson import ObjectId

from src.dto.dto import CreateHotelRequest
from src.repositories.db.mongo_database import MongoDatabase
from src.model.hotel import Hotel

from src.repositories.interfaces.hotel_repository import (
    IHotelRepository
)



class HotelRepository_mango(IHotelRepository):

    def __init__(self):

        self.db = MongoDatabase().get_database()

        self.collection = self.db["hotels"]

    def create(self, hotel: CreateHotelRequest):

        document = {
            "name": hotel.name,
            "city": hotel.city,
            "address": hotel.address,
            "description": hotel.description,
            "rating": 0,
            "tags": [],
            "rooms": []
        }

        result = self.collection.insert_one(document)
        return str(result.inserted_id)

    def get_all(self):

        documents = self.collection.find()
        hotels = []
        for document in documents:
            hotels.append(
                Hotel(
                    id=str(document["_id"]),
                    name=document["name"],
                    city=document["city"],
                    address=document["address"],
                    description=document["description"]
                )
            )

        return hotels

    def get_by_city(self, city: str):

        hotels = self.collection.find(
            {
                "city": city
            }
        )

        result = []

        for hotel in hotels:

            result.append(
                {
                    "id": str(hotel["_id"]),
                    "name": hotel["name"],
                    "city": hotel["city"],
                    "address": hotel["address"],
                    "description": hotel["description"]
                }
            )

        return result

    def get_by_id(self, hotel_id: str):

        hotel = self.collection.find_one(
            {
                "_id": ObjectId(hotel_id)
            }
        )

        if not hotel:
            return None

        return {
            "id": str(hotel["_id"]),
            "name": hotel["name"],
            "city": hotel["city"],
            "address": hotel["address"],
            "description": hotel["description"]
        }
    
    def remove_tag(self, hotel_id: str, tag: str):
        self.collection.update_one(
            {
                "_id": ObjectId(hotel_id)
            },
            {
                "$pull": {
                    "tags": tag
                }
            }
        )

    def add_tag(self, hotel_id: str, tag: str):
        self.collection.update_one(
            {
                "_id": ObjectId(hotel_id)
            },
            {
                "$addToSet": {
                    "tags": tag
                }
            }
        )
