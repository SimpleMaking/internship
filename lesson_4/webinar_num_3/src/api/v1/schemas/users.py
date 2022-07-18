from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserEnter(BaseModel):
    """Вход пользователя"""
    username: str
    password: str

class UserCreate(UserEnter):
    """ Проверяет sign-up запрос """
    email: EmailStr

class UserUpdate(BaseModel):
    '''Обновление данных пользователя'''
    username: str
    email: EmailStr
    
    
class UserBase(BaseModel):
    """ Формирует тело ответа с деталями пользователя """
    uuid: str
    username: str
    email: EmailStr
    is_superuser: bool
    created_at: datetime
    roles: list[str]


class Token(BaseModel):
    access_token: str
   

class RefreshToken(BaseModel):
    refresh_token: str 
   

class Tokens(RefreshToken, Token):
    pass
 


