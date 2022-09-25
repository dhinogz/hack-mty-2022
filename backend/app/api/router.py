from fastapi import APIRouter, Depends

from api.system.views import router as system_router
from api.balance.views import balance_router, transaction_router
from api.user.views import router as user_router
from api.goal.views import router as goal_router

api_router = APIRouter()

api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(user_router, prefix="/user", tags=["user"])
api_router.include_router(balance_router, prefix="/balance", tags=["balance"])
api_router.include_router(transaction_router, prefix="/transaction", tags=["transaction"])
api_router.include_router(goal_router, prefix="/goal", tags=["goal"])

