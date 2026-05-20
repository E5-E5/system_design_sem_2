from pymongo import MongoClient


class MongoDatabase:

    def __init__(self):

        self.client = MongoClient(
            "mongodb://mongo:27017/"
        )

        self.db = self.client["hotel_booking"]

    def get_database(self):

        return self.db