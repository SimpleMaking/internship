from sqlmodel import Session
from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from models import Post
from db import get_db


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get(path="/")
def main(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).filter().all()
    return templates.TemplateResponse('index.html', {'request': request, "posts": posts})


@router.post(path="/main_page")
def main_page(request: Request, post: str = Form(), db: Session = Depends(get_db)):
    post = Post(description=post)
    db.add(post)
    db.commit() 
    db.refresh(post)
    posts = db.query(Post).filter().all()
    return templates.TemplateResponse('index.html', {"request": request, "posts": posts})