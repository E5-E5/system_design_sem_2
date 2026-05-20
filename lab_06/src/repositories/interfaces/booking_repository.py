from abc import ABC, abstractmethod


class IBookingRepository(ABC):

    @abstractmethod
    def create(self, booking):
        pass

    @abstractmethod
    def get_by_user(self, user_id: int):
        pass

    @abstractmethod
    def delete(self, booking_id: int):
        pass