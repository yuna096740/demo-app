from fastapi import FastAPI

from .settings.route import init_route

app = FastAPI()
init_route(app)