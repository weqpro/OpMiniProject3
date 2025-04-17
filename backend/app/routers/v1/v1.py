from fastapi import APIRouter
from .aid_requests import router as aid_requests_router
from .volunteers import router as volunteers_router
from .auth import router as auth_router

router = APIRouter(prefix="/api/v1")
router.include_router(aid_requests_router)
router.include_router(volunteers_router)
router.include_router(auth_router)
