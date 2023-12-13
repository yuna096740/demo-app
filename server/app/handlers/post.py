from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import json
import logging
from typing import Annotated

from app.models.post import Post
from app.libraries.repositories.post import PostRepository
from app.libraries.usecases.post import PostUseCase

from app.settings.database import SessionLocal, get_db

router = APIRouter()
_logger = logging.getLogger(__name__)


@router.post("/post")
async def create_post(
    request: Request,
    post_repo: Annotated[PostRepository, Depends(PostRepository)],
    db: Annotated[Session, Depends(get_db)],
):
    with SessionLocal.begin() as db:
        pass

@router.get("/post")
async def get_post(
    request: Request,
    post_us: Annotated[PostUseCase, Depends(PostUseCase)],
    db: Annotated[Session, Depends(get_db)],
):
    with SessionLocal.begin() as db:
        _logger.info("get all posts")
        posts = post_us.get_posts(db)
        
        return posts