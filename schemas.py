from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    age: int


class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    body: str
    author_id: int


class PostResponse(PostCreate):
    id: int

    class Config:
        orm_mode = True
