from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .api import api_router
from .api.middlewares import TraceIDMiddleware
from .utils import lifespan

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.add_middleware(TraceIDMiddleware)

app.include_router(api_router)
