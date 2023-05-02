from fastapi import APIRouter

from .user_auth import router as user_auth_router

router = APIRouter()
router.include_router(user_auth_router)
