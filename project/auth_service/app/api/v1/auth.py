from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.services.auth_service import register_user, authenticate_user

router = APIRouter()

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register", status_code=201)
def register(data: RegisterRequest):
    if not register_user(data.email, data.password):
        raise HTTPException(status_code=400)
    return

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    token = authenticate_user(data.email, data.password)
    if not token:
        raise HTTPException(status_code=401)
    return {"access_token": token}
