from fastapi import APIRouter

from src.model.hotel import Hotel
from src.services.implementations.hotel_service import HotelService
from fastapi import Depends
from src.security.jwt_middleware import get_current_user

router = APIRouter(prefix="/hotels", tags=["Hotels"])

hotel_service = HotelService()


@router.post("/")
def create_hotel(
    hotel: Hotel,
    user = Depends(get_current_user)
):

    return hotel_service.create_hotel(hotel)


@router.get("/")
def get_hotels():

    return hotel_service.get_hotels()


@router.get("/search")
def get_hotels_by_city(city: str):

    return hotel_service.get_hotels_by_city(city)