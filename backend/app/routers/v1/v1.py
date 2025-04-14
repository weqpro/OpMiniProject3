from fastapi import APIRouter
from .aid_requests import router as aid_requests_router
from .soldiers import router as soldiers_router

router = APIRouter(prefix="/api/v1")
router.include_router(aid_requests_router)
router.include_router(soldiers_router)
