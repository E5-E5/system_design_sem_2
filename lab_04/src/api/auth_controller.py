from fastapi import APIRouter, HTTPException

from src.dto.dto import (
    RegisterRequest,
    LoginRequest
)

from src.model.user import User

from src.services.implementations.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_service = AuthService()


@router.post("/register")
def register(request: RegisterRequest):

    user = User(
        id=request.id,
        login=request.login,
        password=request.password,
        first_name=request.first_name,
        last_name=request.last_name
    )

    created_user = auth_service.register(user)

    if created_user is None:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return created_user


@router.post("/login")
def login(request: LoginRequest):

    result = auth_service.login(
        request.login,
        request.password
    )

    if result is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return result