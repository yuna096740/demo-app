from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import json
import logging
from typing import Annotated

from app.libraries.usecases.post import PostUseCase, CreatePostRequest, UpdatePostRequest, DeletePostRequest

from app.settings.database import SessionLocal, get_db

router = APIRouter()
_logger = logging.getLogger(__name__)


@router.get("/posts")
async def get_post(
    db: Annotated[Session, Depends(get_db)],
    post_us: Annotated[PostUseCase, Depends(PostUseCase)],
):
    with SessionLocal.begin() as db:
        _logger.info("get all posts")
        posts = post_us.get_posts(db)
        
        return posts


@router.post("/post/create")
async def create_post(
    db: Annotated[Session, Depends(get_db)],
    post_usecase: Annotated[PostUseCase, Depends(PostUseCase)],
    post_rq: CreatePostRequest,
):
    with SessionLocal.begin() as db:
        _logger.info("create post")
        
        post = post_usecase.create_post(db, title=post_rq.title, detail=post_rq.detail)
        create_post = {"create_post": post}

    return create_post


@router.patch("/post/update")
async def update_post(
    db: Annotated[Session, Depends(get_db)],
    post_usecase: Annotated[PostUseCase, Depends(PostUseCase)],
    post_rq: UpdatePostRequest,
):
    with SessionLocal.begin() as db:
        _logger.info("update post")
        
        post = post_usecase.update_post(
            db,
            id=post_rq.id,
            title=post_rq.title,
            detail=post_rq.detail
        )
        update_post = {"update_post": post}

    return update_post


@router.delete("/post/delete")
async def delete_post(
    db: Annotated[Session, Depends(get_db)],
    post_usecase: Annotated[PostUseCase, Depends(PostUseCase)],
    post_rq: DeletePostRequest,
):
    with SessionLocal.begin() as db:
        _logger.info("Delete Post")
        
        post = post_usecase.delete_post(
            db,
            id=post_rq.id
        )
        delete_post = {"delete_post": post}

    return delete_post

