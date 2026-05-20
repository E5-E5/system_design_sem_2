from fastapi import APIRouter

from src.dto.dto import CreateHotelRequest
from src.model.hotel import Hotel
from src.services.implementations.hotel_service import HotelService
from fastapi import Depends
from src.security.jwt_middleware import get_current_user
from src.core.limiter import limiter
from fastapi import Request

router = APIRouter(prefix="/hotels", tags=["Hotels"])

hotel_service = HotelService()


@router.post("/")
@limiter.limit("5/minute")
def create_hotel(
    request: Request,
    hotel: CreateHotelRequest,
    user = Depends(get_current_user)
):

    return hotel_service.create_hotel(hotel)


@router.get("/")
@limiter.limit("30/minute")
def get_hotels(request: Request):

    return hotel_service.get_hotels()


@router.get("/search")
@limiter.limit("20/minute")
def get_hotels_by_city(request: Request, city: str):

    return hotel_service.get_hotels_by_city(city)