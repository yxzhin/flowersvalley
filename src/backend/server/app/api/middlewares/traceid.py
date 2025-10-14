import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from .....utils import StructuredLogger, start_time_var, trace_id_var


class TraceIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):  # type: ignore
        trace_id = str(uuid.uuid4())  # Генерируем trace_id
        trace_id_var.set(
            trace_id  # type: ignore
        )  # Устанавливаем trace_id в контекст запроса
        start_time_var.set(time.time())  # type: ignore
        ip = (
            request.headers.get("X-Forwarded-For") or request.client.host
            if request.client
            else "unknown"
        )
        request.state.trace_id = trace_id  # Добавляем trace_id в состояние запроса
        request.state.ip = ip
        StructuredLogger.info("request.start", client_ip=ip)

        response = await call_next(request)  # Выполняем запрос

        StructuredLogger.info(
            "request.end",
        )

        return response
