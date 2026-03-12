from pydantic import BaseModel


class WalletBalanceResponse(BaseModel):
    available_balance: float
    locked_balance: float
    currency: str


class FundWalletRequest(BaseModel):
    amount: float
