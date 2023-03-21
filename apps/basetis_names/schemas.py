import datetime

from pydantic import BaseModel

from apps.users.schemas import UserBase, User


class PostImage(BaseModel):
    image_id: int
    post_id: int
    image: str
    created_at: str
    updated_at: str





class PostCreate(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class Comment(BaseModel):
    comment_id: int
    description: str
    author: User
    type: str
    #replies: list['Comment'] = []
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

Comment.update_forward_refs()

class Post(BaseModel):
    post_id: int
    title: str
    description: str
    type: str
    author: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    #images: list[PostImage]
    #comments: list[Comment]

    class Config:
        orm_mode = True


class BasetisNamePost(Post):
    pass
    #post_id: int

    class Config:
        orm_mode = True



class BasetisNamePostCreate(PostCreate):
    type: str = "basetisname"


class PostImageCreate(BaseModel):
    image: str
