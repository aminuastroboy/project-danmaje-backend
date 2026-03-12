import uuid
from sqlalchemy.orm import Session

from app.models.transaction import Transaction


class TransactionService:
    @staticmethod
    def create_transaction(db: Session, user_id, category: str, amount: float, recipient: str, provider: str = "mock"):
        txn = Transaction(
            reference=f"DMJ-{uuid.uuid4().hex[:10].upper()}",
            user_id=user_id,
            service_category=category,
            amount=amount,
            recipient=recipient,
            provider=provider,
            status="success",
        )
        db.add(txn)
        db.commit()
        db.refresh(txn)
        return txn

    @staticmethod
    def list_transactions(db: Session, user_id):
        return (
            db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .order_by(Transaction.created_at.desc())
            .all()
        )
