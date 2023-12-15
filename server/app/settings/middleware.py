from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.settings.env import Env


def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[Env.API_URL, Env.APP_URL],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )


def init_middleware(app: FastAPI):
    setup_cors(app)