from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    username = Column(String(16),primary_key=True, index=True)
    firstName = Column(String(30))
    lastName = Column(String(80))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

class Post(Base):
    __tablename__ = "posts"
    post_id =

