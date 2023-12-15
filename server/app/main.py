from fastapi import FastAPI

from .settings.route import init_route
from .settings.middleware import init_middleware

app = FastAPI()
init_route(app)
init_middleware(app)