from fastapi import APIRouter, HTTPException

from src.dto.dto import (
    RegisterRequest,
    LoginRequest
)

from src.model.user import User

from src.services.implementations.auth_service import AuthService
from src.core.limiter import limiter
from fastapi import Request

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

auth_service = AuthService()


@router.post("/register")
@limiter.limit("5/minute")
def register(request: Request, request_reg: RegisterRequest):

    user = RegisterRequest(
        login=request_reg.login,
        password=request_reg.password,
        first_name=request_reg.first_name,
        last_name=request_reg.last_name
    )

    created_user = auth_service.register(user)

    if created_user is None:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    return created_user


@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, request_log: LoginRequest):

    result = auth_service.login(
        request_log.login,
        request_log.password
    )

    if result is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return result