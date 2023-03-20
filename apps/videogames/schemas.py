from pydantic import BaseModel

from routers.users.schemas import UserBase

class PostImage(BaseModel):
    image_id: int
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

class Comment(BaseModel):
    comment_id: int
    description: str
    author: UserBase
    type: str
    post_id: int
    replies: list
    created_at: str
    updated_at: str

class Platform(BaseModel):
    platform_id: int
    name: str
    created_at: str
    updated_at: str

class Genre(BaseModel):
    genre_id: int
    name: str
    created_at: str
    updated_at: str

class VideogameBase(BaseModel):
    game_id: int
    title: str
    description: str
    platforms: list[Platform]
    genres: list[Genre]

class Videogame(VideogameBase):
    release_date: str
    publisher: str
    developer: str
    image: str
    created_at: str
    updated_at: str

class VideogamePost(Post):
    videogame: VideogameBase
    valoration: int
    platform: Platform


