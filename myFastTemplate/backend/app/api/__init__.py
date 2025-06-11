from fastapi import APIRouter
from .records import router as record_router

router = APIRouter()
router.include_router(record_router, prefix="/api", tags=["Records"])