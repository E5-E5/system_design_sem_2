from src.model.booking import Booking

from src.repositories.implementations.pg.booking_repository import BookingRepository
from src.services.interfaces.booking_service import (
    IBookingService
)


class BookingService(IBookingService):

    def __init__(self):

        self.booking_repository = BookingRepository()

    def create_booking(self, booking: Booking):

        booking_id = self.booking_repository.create(
            booking
        )

        return {
            "booking_id": booking_id
        }

    def get_user_bookings(self, user_id: int):

        return self.booking_repository.get_by_user(
            user_id
        )

    def cancel_booking(self, booking_id: int):

        return self.booking_repository.delete(
            booking_id
        )