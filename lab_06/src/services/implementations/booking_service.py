from src.model.booking import Booking

from src.repositories.implementations.pg.booking_repository import BookingRepository
from src.services.interfaces.booking_service import (
    IBookingService
)
from src.events.producer import EventProducer


class BookingService(IBookingService):

    def __init__(self):
        self.booking_repository = BookingRepository()
        self.producer = EventProducer()

    def create_booking(self, booking: Booking):
        booking_id = self.booking_repository.create(
            booking
        )

        self.producer.publish(
            "booking.created",
            {
                "booking_id": booking_id,
                "user_id": booking.user_id,
                "hotel_id": booking.hotel_id
            }
        )

        return {
            "booking_id": booking_id
        }

    def get_user_bookings(self, user_id: int):
        return self.booking_repository.get_by_user(
            user_id
        )

    def cancel_booking(self, booking_id: int):
        res = self.booking_repository.delete(booking_id)

        self.producer.publish(
            "booking.canceled", {"res": res}
        )

        return res