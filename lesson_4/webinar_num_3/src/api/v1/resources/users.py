from fastapi import Depends
from src.api.v1.schemas.users import *
from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter
from src.services.auth import AuthService, get_auth_service
from src.api.v1.schemas.users import *

router = APIRouter()

@router.post(path="/api/v1/signup", response_model=dict)
def sing_up(user_data: UserCreate, service: AuthService = Depends(get_auth_service)):
    userinfo = service.register_new_user(user_data=user_data)
    return {"msg": "User created.", "user": dict(list(userinfo)[:-1])}


@router.post(path="/api/v1/login", response_model=Tokens)
def sing_in(form_data: UserEnter, service: AuthService = Depends(get_auth_service)):
    tokens: Tokens = service.authenticate_user(form_data.username, form_data.password)
    return tokens


@router.get(path="/api/v1/users/me", response_model=dict)
def get_user_info(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/login")), service: AuthService = Depends(get_auth_service)):
    user_profile_info = service.get_profile_info(token)
    return {"user": user_profile_info}


@router.patch(path="/api/v1/users/me", response_model=dict)
def info_refresh(user_data: UserUpdate, service: AuthService = Depends(get_auth_service), token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/login"))):
   user_update_info = service.get_updating_info(user_data, token)
   return user_update_info

@router.post(path="/api/v1/refresh", response_model=Tokens)
def token_refresh(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/v1/login")), service: AuthService = Depends(get_auth_service)):
    tokens: Tokens = service.get_new_tokens(token)
    return tokens


