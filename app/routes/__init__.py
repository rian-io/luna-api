# app/api/routes/__init__.py
from fastapi import APIRouter
from . import auth, users

router = APIRouter()
router.include_router(auth.router)
router.include_router(users.router)
