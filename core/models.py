import enum
from sqlalchemy import Enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    username = Column(String(16), primary_key=True, index=True)
    first_name = Column(String(30))
    last_name = Column(String(80))
    email = Column(String(255), unique=True, index=True)
    password = Column(Text)
    is_active = Column(Boolean, default=True)
    posts = relationship("Post", back_populates="author")


class Post(Base):
    __tablename__ = "posts"
    post_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(127))
    description = Column(Text())
    type = Column(String(16))
    author_id = Column(String(16), ForeignKey("users.username"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    comments = relationship("Comment", back_populates="post")
    images = relationship("PostImage", back_populates="post")
    author = relationship("User", back_populates="posts")
    __mapper_args__ = {
        "polymorphic_identity": "post",
        "polymorphic_on": "type",
    }


class CommentType(str, enum.Enum):
    post = "post"
    reply = "reply"


class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer, primary_key=True, index=True)
    description = Column(Text())
    author_id = Column(String(16), ForeignKey("users.username"))
    type = Column(Enum(CommentType))
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    replies_id = Column(Integer, ForeignKey("comments.comment_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    post = relationship("Post", back_populates="comments")
    replies = relationship("Comment")
    author = relationship("User")


class PostImage(Base):
    __tablename__ = "post_images"
    image_id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.post_id"))
    image = Column(Text())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    post = relationship("Post", back_populates="images")


class Platform(Base):
    __tablename__ = "platforms"
    platform_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Genre(Base):
    __tablename__ = "genres"
    genre_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class Videogame(Base):
    __tablename__ = "videogames"
    game_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(127))
    description = Column(Text())
    release_date = Column(DateTime(timezone=True))
    publisher = Column(String(127))
    developer = Column(String(127))
    genre_id = Column(Integer, ForeignKey("genres.genre_id"))
    image = Column(Text())
    platform_id = Column(Integer, ForeignKey("platforms.platform_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class VideogamePost(Post):
    __tablename__ = "videogame_posts"
    valoration = Column(Integer)
    post_id = Column(Integer, ForeignKey("posts.post_id"), primary_key=True)
    game_id = Column(Integer, ForeignKey("videogames.game_id"))
    platform_id = Column(Integer, ForeignKey("platforms.platform_id"))
    __mapper_args__ = {
        "polymorphic_identity": "videogame",
    }


class BasetisNamePost(Post):
    __tablename__ = "basetis_name_posts"
    post_id = Column(Integer, ForeignKey("posts.post_id"), primary_key=True)
    __mapper_args__ = {
        "polymorphic_identity": "basetisname",
    }
