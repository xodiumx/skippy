from fastapi import APIRouter
from .test import router as test

router = APIRouter()
router.include_router(test)