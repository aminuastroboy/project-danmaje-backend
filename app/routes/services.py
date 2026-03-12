from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.deps import get_current_user
from app.models.user import User
from app.schemas.service import BuyAirtimeRequest, BuyDataRequest
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/services", tags=["Services"])


@router.post("/airtime")
def buy_airtime(
    payload: BuyAirtimeRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    txn = TransactionService.create_transaction(
        db=db,
        user_id=current_user.id,
        category="airtime",
        amount=payload.amount,
        recipient=payload.phone,
        provider="mock-vtu",
    )
    return {"message": "Airtime purchase simulated", "reference": txn.reference, "status": txn.status}


@router.post("/data")
def buy_data(
    payload: BuyDataRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    txn = TransactionService.create_transaction(
        db=db,
        user_id=current_user.id,
        category="data",
        amount=payload.amount,
        recipient=payload.phone,
        provider="mock-vtu",
    )
    return {"message": "Data purchase simulated", "reference": txn.reference, "status": txn.status, "plan": payload.plan}
