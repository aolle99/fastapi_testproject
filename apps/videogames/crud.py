from sqlalchemy.orm import Session

from apps.videogames import schemas
from apps.users import schemas as user_schemas
from core import models


def create_post(db: Session, post: schemas.VideogamePostCreate, user: user_schemas.UserBase):
    db_videogamepost = models.VideogamePost(**post.dict(), author_id=user.username, type="videogame")
    db.add(db_videogamepost)
    db.commit()
    db.refresh(db_videogamepost)
    return db_videogamepost


def get_videogameposts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.VideogamePost).offset(skip).limit(limit).all()

def get_videogamepost(db: Session, post_id: int):
    return db.query(models.VideogamePost).filter(models.VideogamePost.post_id == post_id).first()


def get_videogames(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Videogame).offset(skip).limit(limit).all()


def get_platforms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Platform).offset(skip).limit(limit).all()


def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Genre).offset(skip).limit(limit).all()
