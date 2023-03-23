from sqlalchemy.orm import Session

from core import models
from . import schemas


def get_post(db: Session, post_id: int):
    return db.query(models.BasetisNamePost).filter(models.BasetisNamePost.post_id == post_id).first()


def get_names(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.BasetisNamePost).offset(skip).limit(limit).all()


def create_post(db: Session, post: schemas.BasetisNamePostCreate, user: schemas.UserBase):
    db_basetisname = models.BasetisNamePost(**post.dict(), author_id=user.username, type="basetisname")
    db.add(db_basetisname)
    db.commit()
    db.refresh(db_basetisname)
    return db_basetisname


def update_post(db: Session, post: schemas.BasetisNamePostCreate, post_id: int):
    db_post = get_post(db, post_id)
    db_post.title = post.title
    db_post.description = post.description
    db.commit()
    db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = get_post(db, post_id)
    if db_post is None:
        return None
    db.delete(db_post)
    db.commit()
    return db_post
