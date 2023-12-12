from fastapi import Depends, Request, HTTPException
from typing import Annotated

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.post import PostOrm, Post
from app.settings.database import get_db



class PostRepository:
    def create_post(
        self,
        db: Session,
        post_id: int,
        title: str,
        detail: str,
    ) -> Post:
        post = db.scalars((
            select(PostOrm)
            .with_for_update()
            .where(PostOrm.id == post_id)
        )).one_or_none()
        
        if post is None:
            post = PostOrm(
                title=title,
                detail=detail
            )

        db.add(post)
        db.flush()
        return PostOrm.from_orm(post)
    
    def get_posts(
        self,
        db: Annotated[Session, Depends(get_db)],
        post_id: int,
    ):
        post_orm = db.scalars(
            (
                select(PostOrm)
                .filter(PostOrm.id == post_id)
            )
        ).all()
        
        return PostOrm.from_orm(post_orm)