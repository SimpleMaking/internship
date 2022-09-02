from sqlmodel import Session
from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
#from db import get_session
#from flask_wtf import FlaskForm
from wtforms import Form, TextAreaField, SubmitField, validators
from models import Post
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from db import get_db
#from flask import render_template

router = APIRouter()
templates = Jinja2Templates(directory="templates")
class PostForm(Form):
    body = TextAreaField("What's on your mind?")#, validators=[Required()])
    submit = SubmitField('Submit')
    

@router.get(path="/")    #, response_class=HTMLResponse)#, methods=['GET', 'POST'])
def main_page(request: Request, db: Session = Depends(get_db)):
    form = PostForm()
    if form.validate():
        post = Post(description=form.body.data)
        db.add(post)
        return RedirectResponse(Request.url_for(name='.main_page', self=request))
    
    #posts = "!!!"
    posts = db.query(Post).all()
    return templates.TemplateResponse('index.html', {"request": request, "form": form, "posts": posts})
  

    