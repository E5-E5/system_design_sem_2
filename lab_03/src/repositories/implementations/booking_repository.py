from src.model.booking import Booking

from src.repositories.implementations.database import Database
from src.repositories.interfaces.booking_repository import (
    IBookingRepository
)


class BookingRepository(IBookingRepository):

    def __init__(self):

        self.db = Database()

    def create(self, booking: Booking):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        INSERT INTO bookings (
            user_id,
            hotel_id,
            check_in,
            check_out
        )
        VALUES (%s, %s, %s, %s)
        RETURNING id;
        """

        cursor.execute(
            query,
            (
                booking.user_id,
                booking.hotel_id,
                booking.check_in,
                booking.check_out
            )
        )

        booking_id = cursor.fetchone()[0]

        connection.commit()

        cursor.close()

        return booking_id

    def get_by_user(self, user_id: int):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        SELECT
            id,
            user_id,
            hotel_id,
            check_in,
            check_out
        FROM bookings
        WHERE user_id = %s;
        """

        cursor.execute(query, (user_id,))

        rows = cursor.fetchall()

        cursor.close()

        bookings = []

        for row in rows:

            bookings.append(
                Booking(
                    id=row[0],
                    user_id=row[1],
                    hotel_id=row[2],
                    check_in=row[3],
                    check_out=row[4]
                )
            )

        return bookings

    def delete(self, booking_id: int):

        connection = self.db.get_connection()

        cursor = connection.cursor()

        query = """
        DELETE FROM bookings
        WHERE id = %s;
        """

        cursor.execute(query, (booking_id,))

        connection.commit()

        deleted_rows = cursor.rowcount

        cursor.close()

        return deleted_rows > 0