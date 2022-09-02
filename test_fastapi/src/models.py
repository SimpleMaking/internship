from sqlalchemy import Column, Integer, Text
from db import Base

class Post(Base):
    __tablename__ = "posts"
    id: int = Column(Integer, primary_key=True, index=True)
    description: str = Column(Text, default=None)
