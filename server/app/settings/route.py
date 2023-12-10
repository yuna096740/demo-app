from fastapi import FastAPI

from app.handlers import (
    debug,
)

def init_route(app: FastAPI) -> None:
    app.include_router(debug.router)