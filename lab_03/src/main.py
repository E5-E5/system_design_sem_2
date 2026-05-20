from fastapi import FastAPI

from src.api.auth_controller import router as auth_router
from src.api.users_controller import router as users_router
from src.api.hotels_controller import router as hotels_router
from src.api.bookings_controller import router as bookings_router

app = FastAPI(
    title="Hotel Booking API",
    description="REST API for hotel booking system",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(hotels_router)
app.include_router(bookings_router)