from fastapi import APIRouter, HTTPException

from src.model.booking import Booking
from src.services.implementations.booking_service import BookingService
from fastapi import Depends
from src.security.jwt_middleware import get_current_user
from src.core.limiter import limiter
from fastapi import Request

router = APIRouter(prefix="/bookings", tags=["Bookings"])

booking_service = BookingService()


@router.post("/")
@limiter.limit("5/minute")
def create_booking(
    request: Request,
    booking: Booking,
    user = Depends(get_current_user)
):

    return booking_service.create_booking(booking)


@router.get("/{user_id}")
@limiter.limit("5/minute")
def get_user_bookings(request: Request, user_id: int):

    return booking_service.get_user_bookings(user_id)


@router.delete("/{booking_id}")
@limiter.limit("5/minute")
def cancel_booking(request: Request, booking_id: int):

    result = booking_service.cancel_booking(booking_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return {
        "message": "Booking cancelled"
    }