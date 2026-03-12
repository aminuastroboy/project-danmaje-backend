import uuid
from sqlalchemy import Column, String, DateTime, func, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.db import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    available_balance = Column(Numeric(12, 2), default=0)
    locked_balance = Column(Numeric(12, 2), default=0)
    currency = Column(String, default="NGN")
    status = Column(String, default="active")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
