from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import get_current_user
from app.models.user import User
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("")
def list_transactions(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    txns = TransactionService.list_transactions(db, current_user.id)
    return [
        {
            "reference": t.reference,
            "category": t.service_category,
            "amount": float(t.amount),
            "status": t.status,
            "recipient": t.recipient,
            "created_at": t.created_at,
        }
        for t in txns
    ]
