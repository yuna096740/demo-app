from fastapi import FastAPI

from app.handlers import (
    debug, post
)

def init_route(app: FastAPI) -> None:
    app.include_router(debug.router)
    app.include_router(post.router)