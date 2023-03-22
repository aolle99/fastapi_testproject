import datetime
import enum

from pydantic import BaseModel, AnyHttpUrl

from apps.users.schemas import UserBase, User


class PostImage(BaseModel):
    image_id: int
    image: AnyHttpUrl
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

    class Config:
        orm_mode = True


class PostImageCreate(BaseModel):
    image: AnyHttpUrl


class CommentType(str, enum.Enum):
    post = "post"
    reply = "reply"


class Comment(BaseModel):
    comment_id: int
    description: str
    author: User
    type: CommentType
    replies: list['Comment'] = []
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

    class Config:
        orm_mode = True
        use_enum_values = True


Comment.update_forward_refs()


class CommentCreate(BaseModel):
    description: str


class Post(BaseModel):
    post_id: int
    title: str
    description: str
    type: str
    author: User
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    images: list[PostImage]
    comments: list[Comment]

    class Config:
        orm_mode = True


class PostCreate(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True
