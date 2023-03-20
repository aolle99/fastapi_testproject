import self as self
from pydantic import BaseModel

from routers.users.schemas import UserBase

class PostImage(BaseModel):
    image_id: int
    post_id: int
    image: str
    created_at: str
    updated_at: str
class Post(BaseModel):
    post_id: int
    title: str
    description: str
    type: str
    author: UserBase
    created_at: str
    updated_at: str
    images: list[PostImage]

class PostCreate(BaseModel):
    title: str
    description: str

class Comment(BaseModel):
    comment_id: int
    description: str
    author: UserBase
    type: str
    created_at: str
    updated_at: str

class BasetisNamePost(Post):
    images: list[PostImage]
    comments: list[Comment]

class BasetisNamePostCreate(PostCreate):
    type: str = "basetisname"


class PostImageCreate(BaseModel):
    image: str