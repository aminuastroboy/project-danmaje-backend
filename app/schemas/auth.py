from pydantic import BaseModel, EmailStr


class RegisterRequest(BaseModel):
    full_name: str
    phone: str
    email: EmailStr | None = None
    password: str


class LoginRequest(BaseModel):
    phone: str
    password: str


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
