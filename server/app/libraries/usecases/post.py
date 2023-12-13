from fastapi import Depends, Request

from typing import Annotated, List
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.libraries.repositories.post import PostRepository


class PostRequest(BaseModel):
    id: int
    title: str
    detail: str
    created_at: datetime
    updated_at: datetime


class PostUseCase:
    def __init__(
        self,
        post_repo: Annotated[PostRepository, Depends(PostRepository)],
    ):
        self.post_repo = post_repo
    
    def get_posts(
        self,
        db: Session
    ) -> List[PostRequest]:
        posts = self.post_repo.get_posts(db)
        post_list = []
        for post in posts:
            post_data = PostRequest(
                id=post.id,
                title=post.title,
                detail=post.detail,
                created_at=post.created_at,
                updated_at=post.updated_at,
            )
            post_list.append(post_data)
        
        return post_list