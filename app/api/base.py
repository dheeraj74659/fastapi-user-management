"""
Base file for consolidated imports.
"""
from app.api.v1 import auth, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(auth.router, prefix="", tags=["auth"])
api_router.include_router(users.router, prefix="", tags=["users"])