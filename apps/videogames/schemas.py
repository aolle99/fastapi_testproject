import datetime

from pydantic import BaseModel

from apps.posts.schemas import Post

class Platform(BaseModel):
    platform_id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

class Genre(BaseModel):
    genre_id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None

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
    valoration: int
    game_id: int
    platform_id: int




