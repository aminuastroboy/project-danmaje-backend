from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, AuthResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    try:
        token = AuthService.register(db, payload)
        return {"access_token": token}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        token = AuthService.login(db, payload.phone, payload.password)
        return {"access_token": token}
    except ValueError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
