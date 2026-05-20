from pydantic import BaseModel


class RegisterRequest(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str


class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str


class CreateHotelRequest(BaseModel):
    name: str
    city: str
    address: str
    description: str


class HotelResponse(BaseModel):
    id: str
    name: str
    city: str
    address: str
    description: str


class CreateBookingRequest(BaseModel):
    hotel_id: str
    check_in: str
    check_out: str


class BookingResponse(BaseModel):
    id: int
    user_id: int
    hotel_id: str
    check_in: str
    check_out: str

