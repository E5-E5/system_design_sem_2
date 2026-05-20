from src.dto.dto import CreateHotelRequest
from src.model.hotel import Hotel

from src.repositories.db.pg_database import Database
from src.repositories.interfaces.hotel_repository import (
    IHotelRepository
)


class HotelRepository(IHotelRepository):

    def __init__(self):

        self.db = Database()

    def create(self, hotel: CreateHotelRequest):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO hotels (
            name,
            city,
            address,
            description
        )
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """

        cursor.execute(
            query,
            (
                hotel.name,
                hotel.city,
                hotel.address,
                hotel.description
            )
        )

        hotel_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()

        return hotel_id

    def get_all(self):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        SELECT
            id,
            name,
            city,
            address,
            description
        FROM hotels;
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        cursor.close()

        hotels = []

        for row in rows:

            hotels.append(
                Hotel(
                    id=row[0],
                    name=row[1],
                    city=row[2],
                    address=row[3],
                    description=row[4]
                )
            )

        return hotels

    def get_by_city(self, city: str):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        SELECT
            id,
            name,
            city,
            address,
            description
        FROM hotels
        WHERE city = %s;
        """

        cursor.execute(query, (city,))

        rows = cursor.fetchall()

        cursor.close()

        hotels = []

        for row in rows:

            hotels.append(
                Hotel(
                    id=row[0],
                    name=row[1],
                    city=row[2],
                    address=row[3],
                    description=row[4]
                )
            )

        return hotels

    def get_by_id(self, hotel_id: int):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        SELECT
            id,
            name,
            city,
            address,
            description
        FROM hotels
        WHERE id = %s;
        """

        cursor.execute(query, (hotel_id,))

        row = cursor.fetchone()

        cursor.close()

        if row is None:
            return None

        return Hotel(
            id=row[0],
            name=row[1],
            city=row[2],
            address=row[3],
            description=row[4]
        )