from pydantic import BaseModel


class BuyAirtimeRequest(BaseModel):
    network: str
    phone: str
    amount: float


class BuyDataRequest(BaseModel):
    network: str
    phone: str
    plan: str
    amount: float
