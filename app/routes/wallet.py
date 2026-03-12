from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import get_current_user
from app.models.user import User
from app.schemas.wallet import WalletBalanceResponse
from app.services.wallet_service import WalletService

router = APIRouter(prefix="/wallet", tags=["Wallet"])


@router.get("/balance", response_model=WalletBalanceResponse)
def get_balance(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return WalletService.get_balance(db, current_user.id)
