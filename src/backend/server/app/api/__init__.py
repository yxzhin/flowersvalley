from fastapi import APIRouter

from .routes import *

api_router = APIRouter()
api_router.include_router(test_router)
