from fastapi import APIRouter
from app.routes.auth import router as auth_router
from app.routes.wallet import router as wallet_router
from app.routes.services import router as services_router
from app.routes.transactions import router as transactions_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(wallet_router)
api_router.include_router(services_router)
api_router.include_router(transactions_router)
