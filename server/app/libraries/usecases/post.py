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

class CreatePostRequest(BaseModel):
    title: str
    detail: str

class UpdatePostRequest(BaseModel):
    id: int
    title: str
    detail: str

class DeletePostRequest(BaseModel):
    id: int


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
    
    def create_post(
        self,
        db: Session,
        title: str,
        detail: str,
    ) -> CreatePostRequest:
        post = self.post_repo.create_post(db, title, detail)
        return post


    def update_post(
        self,
        db: Session,
        id: int,
        title: str,
        detail: str,
    ) -> UpdatePostRequest:
        post = self.post_repo.update_post(db, id, title, detail)
        return post