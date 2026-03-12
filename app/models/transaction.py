import uuid
from sqlalchemy import Column, String, DateTime, func, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from app.db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    reference = Column(String, unique=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    service_category = Column(String, nullable=False)
    service_code = Column(String, nullable=True)
    provider = Column(String, nullable=True)
    amount = Column(Numeric(12, 2), nullable=False)
    fee = Column(Numeric(12, 2), default=0)
    status = Column(String, default="pending")
    provider_reference = Column(String, nullable=True)
    recipient = Column(String, nullable=True)
    meta_json = Column(JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
