from app.settings.env import Env
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

_database_url = URL.create(
    drivername="mysql+mysqldb",
    username=Env.DATABASE_USER,
    password=Env.DATABASE_PASSWORD,
    host=Env.DATABASE_HOST,
    port=Env.DATABASE_PORT,
    database=Env.DATABASE_NAME
)
Engine = create_engine(_database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=Engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()