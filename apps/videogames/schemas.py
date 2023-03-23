import datetime

from pydantic import BaseModel

from apps.posts.schemas import Post, PostCreate


class Platform(BaseModel):
    platform_id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    class Config:
        orm_mode = True


class Genre(BaseModel):
    genre_id: int
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    class Config:
        orm_mode = True


class VideogameBase(BaseModel):
    game_id: int
    title: str
    description: str | None
    platforms: Platform
    genres: Genre

    class Config:
        orm_mode = True


class Videogame(VideogameBase):
    release_date: datetime.datetime | None
    publisher: str
    developer: str
    image: str | None
    created_at: datetime.datetime
    updated_at: datetime.datetime | None
    class Config:
        orm_mode = True


class VideogamePost(Post):
    valoration: int
    games: Videogame
    platform: Platform
    class Config:
        orm_mode = True


class VideogamePostCreate(PostCreate):
    valoration: int
    game_id: int
    platform_id: int
