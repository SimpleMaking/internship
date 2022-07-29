from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel



__all__ = ("Post", "User",)
class User(SQLModel, table=True):
    __tablename__ = "users"
    uuid: str = Field(default=None, primary_key=True)
    username: str = Field(nullable=False)
    roles: list[str] = Field(default=None)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    is_superuser: bool = Field(default=False)
    is_totp_enabled: bool = Field(default=False)
    is_active: bool = Field(default=True)
    email: str = Field(nullable=False)
    password_hash: str = Field(nullable=False)


class Post(SQLModel, table=True):
    __tablename__ = "posts"
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: str = Field(nullable=False)
    views: int = Field(default=0)
    #user_uuid: str = Field(foreign_key="users.uuid")
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

