from fastapi import APIRouter, HTTPException

from src.services.implementations.user_service import UserService


router = APIRouter(prefix="/users", tags=["Users"])

user_service = UserService()


@router.get("/{login}")
def get_user_by_login(login: str):

    user = user_service.get_by_login(login)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get("/")
def search_users(name: str):

    return user_service.search_users(name)