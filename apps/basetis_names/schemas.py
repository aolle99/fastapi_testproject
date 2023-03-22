import datetime

from pydantic import BaseModel, AnyHttpUrl

from apps.posts.schemas import Post, PostCreate
from apps.users.schemas import UserBase, User





class BasetisNamePost(Post):
    pass
    #post_id: int

    class Config:
        orm_mode = True



class BasetisNamePostCreate(PostCreate):
    pass


