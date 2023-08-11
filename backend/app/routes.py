from app.modules.shift import api_router as shift_router
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(shift_router, prefix="/shift", tags=["Shift"])
