from redis.asyncio import Redis

from ....utils import StructuredLogger
from ..conf import Config


class RedisService:
    _redis: Redis | None = None
    auth_state_prefix = "auth_state:"

    @classmethod
    async def init(cls) -> None:
        """Инициализация пула соединений с Redis."""
        cls._redis = Redis(
            host=Config.REDIS_HOST,  # type: ignore
            port=Config.REDIS_PORT,  # type: ignore
            decode_responses=True,
            max_connections=20,
        )
        try:
            if await cls._redis.ping():  # type: ignore
                StructuredLogger.info("redis.connected")
        except Exception as e:
            StructuredLogger.exception("redis.connection_error", error=str(e))
            raise e

    @classmethod
    async def close(cls) -> None:
        """Закрытие соединения с Redis."""
        if cls._redis:
            await cls._redis.close()
            StructuredLogger.info("redis.closed")
