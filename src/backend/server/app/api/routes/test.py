from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from ...db import Database
from ...db.models import User
from ..responses import TestResponse

test_router = APIRouter(prefix="/test")


@test_router.get("/", response_model=TestResponse)
async def test(session: AsyncSession = Depends(Database.dependency)) -> Any:
    query = select(func.count()).select_from(User)
    users_count = await session.scalar(query)
    return {"message": "it works!! :tada:", "users_count": users_count}
