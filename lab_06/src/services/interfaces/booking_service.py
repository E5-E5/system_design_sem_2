from abc import ABC, abstractmethod

from src.model.booking import Booking

class IBookingService(ABC):

    @abstractmethod
    def create_booking(self, booking: Booking):
        pass

    @abstractmethod
    def get_user_bookings(self, user_id: int):
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int):
        pass