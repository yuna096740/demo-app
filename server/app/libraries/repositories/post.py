from fastapi import Depends, Request, HTTPException
from typing import Annotated

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.post import PostOrm, Post
from app.settings.database import get_db



class PostRepository:
    def get_posts(
        self,
        db: Annotated[Session, Depends(get_db)],
    ):
        post_orm = db.scalars((
            select(PostOrm)
        )).all()
        return post_orm


    def create_post(
        self,
        db: Session,
        title: str,
        detail: str,
    ) -> PostOrm:
        exist_post = db.scalar((
            select(PostOrm)
            .filter(PostOrm.id == id)
        )).one_or_none()
        
        if exist_post is None:
            new_post = PostOrm(
                title=title,
                detail=detail,
            )
        else:
            return HTTPException(
                status_code=404, detail="There Is Not Post"
            )
        db.add(new_post)
        db.flush()
        
        post = new_post.title, new_post.detail
        return post


    def update_post(
        self,
        db: Session,
        id: int,
        title: str,
        detail: str,
    ):
        exist_post = db.scalar((
            select(PostOrm)
            .filter(PostOrm.id == id)
        ))

        if exist_post is None:
            return HTTPException(
                status_code=404, detail="There Is Not Same Post"
            )
        else:
            exist_post.title = title
            exist_post.detail = detail
        db.flush()

        post = title, detail
        return post


    def delete_post(
        self,
        db: Session,
        id: int,
    ) -> int:
        exist_post = db.scalar((
            select(PostOrm)
            .filter(PostOrm.id == id)
        ))

        if exist_post is None:
            return HTTPException(
                status_code=404, detail="There Is Not Post"
            )
        else:
            db.delete(exist_post)
            db.flush

        post = "Success"
        return post