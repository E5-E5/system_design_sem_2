from fastapi import APIRouter, HTTPException

from src.services.implementations.user_service import UserService
from src.core.limiter import limiter
from fastapi import Request

router = APIRouter(prefix="/users", tags=["Users"])

user_service = UserService()


@router.get("/{login}")
@limiter.limit("5/minute")
def get_user_by_login(request: Request, login: str):

    user = user_service.get_by_login(login)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/")
@limiter.limit("5/minute")
def search_users(request: Request, name: str):

    return user_service.search_users(name)