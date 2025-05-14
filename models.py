from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import base


class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True, nullable=False)
    age = Column(Integer, nullable=False)

    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', age={self.age})>"


class Post(base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True, nullable=False)
    body = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")

    def __repr__(self):
        return f"<Post(id={self.id}, title='{self.title}', author_id={self.author_id})>"
