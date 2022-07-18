from sqlmodel import Session, create_engine
from src.core import config
from sqlmodel import SQLModel
#from sqlalchemy.ext.declarative import declarative_base

__all__ = ("get_session",)

engine = create_engine(config.DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
