from pydantic import BaseModel

class Booking(BaseModel):
    id: int
    user_id: int
    hotel_id: str
    check_in: str
    check_out: str