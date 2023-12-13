import datetime
from sqlalchemy import Column, ForeignKey, DateTime, BigInteger, String, Boolean

from pydantic import BaseModel
from app.settings.database import Base

class PostOrm(Base):
    __tablename__ = "post"
    
    id = Column(BigInteger, primary_key=True, nullable=False)
    title = Column(String(80), nullable=False)
    detail = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
    )

class Post(BaseModel):
    id: int
    title: str
    detail: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    
    class Config:
        orm_mode = True