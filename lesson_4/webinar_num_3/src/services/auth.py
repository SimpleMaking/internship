from datetime import datetime, timedelta
from logging import exception
from pydantic import ValidationError
from passlib.hash import bcrypt
from jose import JWTError, jwt
from sqlmodel import Session
from src.core import config
from fastapi import Depends, HTTPException, status 
from src.models import db 
from src.api.v1.schemas.users import Token, Tokens, UserCreate, UserUpdate
from src.models import User
from src.services import ServiceMixin
from src.db import AbstractCache, get_cache, get_session
from functools import lru_cache
from uuid import uuid4
    
class AuthService(ServiceMixin):

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)
        
        
    def hash_password(self, password: str) -> str:
        return bcrypt.hash(password)
    
    
    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="could not validate credentials", headers={'WWW-Authenticate': 'Bearer'})
        
        try:
            payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
        except JWTError:
            raise exception 
            
        user_data = payload.get('user')
        
        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None
        
        return user 
      
      
    def create_tokens(self, user: db.User) -> Tokens:
        user_data = User.from_orm(user)
        
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'ref': now,
            'exp': now + timedelta(days=0, minutes=config.JWT_EXPIRATION),
            'scope': 'access_token',
            'user': user_data.dict(),
        }
        access_token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
        payload = {
            'iat': now,
            'ref': now,
            'exp': now + timedelta(days=0, hours=20),
            'scope': 'refresh_token',
            'user': user_data.dict(),
        }
        refresh_token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
        
        return Tokens(access_token=access_token, refresh_token=refresh_token)
    
    
    def create_token(self, user: db.User) -> Token:
        user_data = User.from_orm(user)
        
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'ref': now,
            'exp': now + timedelta(days=0, minutes=config.JWT_EXPIRATION),
            'scope': 'access_token',
            'user': user_data.dict(),
        }
        access_token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
        return Token(access_token=access_token)
  
   
    def register_new_user(self, user_data: UserCreate) -> User:
        exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="this username is already in use", headers={'WWW-Authenticate': 'Bearer'})
        user = User(email=user_data.email, username=user_data.username, password_hash=self.hash_password(user_data.password), uuid=str(uuid4())) 
        all_users = self.session.query(User).filter().all()
        for value in all_users:
            if user.username == value.username:
                raise exception
            
        self.session.add(user)
        self.session.commit() 
        self.session.refresh(user)
        
        return user
    
    
    def authenticate_user(self, username: str, password: str) -> Tokens:
        exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="incorrect username or password", headers={'WWW-Authenticate': 'Bearer'})
        user = self.session.query(User).filter(User.username == username).first()
        
        if not user:
            raise exception
        
        if not self.verify_password(password, user.password_hash):
            raise exception
      
        return self.create_tokens(user)
    
    
    
    def get_profile_info(self, token: str) -> User:
        user = self.validate_token(token)
        user = dict(user)
        user.pop("password_hash")
        user.pop("is_totp_enabled")
        user.pop("is_active")
        return user
    
    
    def get_updating_info(self, user_data: UserUpdate, token: str) -> dict:
        exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data not found", headers={'WWW-Authenticate': 'Bearer'})
        user = self.validate_token(token)
        user_from_db = self.session.query(User).filter(User.username==user.username).first()
        if user_from_db:
            user_from_db.username = user_data.username
            user_from_db.email = user_data.email
        else:
            raise exception
        token: Token = self.create_token(user_from_db)
        
        return {"msg": "Update is successful. Please use new access_token.", "user": dict(list(user_from_db)[:-1]), "access_token": token.access_token} 
    
    
    def get_new_tokens(self, token: str) -> Tokens:
        cur_user: User = AuthService.validate_token(token)
        return self.create_tokens(cur_user)    
        
@lru_cache()
def get_auth_service(
    cache: AbstractCache = Depends(get_cache),
    session: Session = Depends(get_session),
) -> AuthService:
    return AuthService(cache=cache, session=session)