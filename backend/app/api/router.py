from fastapi import APIRouter

from api.system.views import router as system_router
from api.auth.views import router as auth_router


api_router = APIRouter()
api_router.include_router(system_router, prefix="/system", tags=["system"])
api_router.include_router(auth_router, prefix="", tags=["auth"])