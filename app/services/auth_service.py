from sqlalchemy.orm import Session

from app.models.user import User
from app.models.wallet import Wallet
from app.schemas.auth import RegisterRequest
from app.utils.security import hash_password, verify_password, create_access_token


class AuthService:
    @staticmethod
    def register(db: Session, payload: RegisterRequest):
        existing = db.query(User).filter(User.phone == payload.phone).first()
        if existing:
            raise ValueError("Phone number already registered")

        user = User(
            full_name=payload.full_name,
            phone=payload.phone,
            email=payload.email,
            password_hash=hash_password(payload.password),
        )
        db.add(user)
        db.flush()

        wallet = Wallet(user_id=user.id)
        db.add(wallet)
        db.commit()
        db.refresh(user)

        return create_access_token(str(user.id))

    @staticmethod
    def login(db: Session, phone: str, password: str):
        user = db.query(User).filter(User.phone == phone).first()
        if not user or not verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")
        return create_access_token(str(user.id))
