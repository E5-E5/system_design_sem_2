from src.model.booking import Booking
from src.services.interfaces.booking_service import IBookingService


class BookingService(IBookingService):

    def __init__(self):
        self.bookings = []

    def create_booking(self, booking: Booking):

        self.bookings.append(booking)

        return booking

    def get_user_bookings(self, user_id: int):

        result = []

        for booking in self.bookings:

            if booking.user_id == user_id:
                result.append(booking)

        return result

    def cancel_booking(self, booking_id: int):

        for booking in self.bookings:

            if booking.id == booking_id:

                self.bookings.remove(booking)

                return True

        return False