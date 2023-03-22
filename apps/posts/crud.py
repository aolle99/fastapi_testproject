from sqlalchemy.orm import Session

from core import models
from . import schemas


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.post_id == post_id).first()


def create_comment(db: Session, post: schemas.CommentCreate, user: schemas.UserBase, comment_type: str, post_id: int | None=None,comment_id: int | None=None):
    db_post_comment = models.Comment(**post.dict(), author_id=user.username, type=comment_type, post_id=post_id, replies_id=comment_id)
    db.add(db_post_comment)
    db.commit()
    db.refresh(db_post_comment)
    return db_post_comment


def upload_post_image(db: Session, image: schemas.PostImageCreate, post_id: int):
    db_image = models.PostImage(image=image.image, post_id=post_id)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image