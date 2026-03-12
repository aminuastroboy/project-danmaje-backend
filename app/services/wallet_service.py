from sqlalchemy.orm import Session

from app.models.wallet import Wallet


class WalletService:
    @staticmethod
    def get_balance(db: Session, user_id):
        wallet = db.query(Wallet).filter(Wallet.user_id == user_id).first()
        if not wallet:
            raise ValueError("Wallet not found")
        return {
            "available_balance": float(wallet.available_balance),
            "locked_balance": float(wallet.locked_balance),
            "currency": wallet.currency,
        }
