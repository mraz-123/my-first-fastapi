from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, session_local, base
from models import User, Post
from schemas import UserCreate, PostCreate, UserResponse, PostResponse
from typing import List

app = FastAPI()

base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


@app.post("/user/add", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/posts/add", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    author = db.query(User).filter(User.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    new_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts", response_model=List[PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return db.query(Post).all()


@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post
