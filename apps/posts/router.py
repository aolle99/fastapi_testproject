from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from . import crud, schemas
from apps.users import schemas as user_schema
from core.database import get_db
from ..users.router import get_current_active_user

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
)


@router.post("/{post_id}/comments", response_model=schemas.Comment, status_code=201)
def create_post_comment(
        post: schemas.CommentCreate,
        post_id: int,
        current_user: Annotated[user_schema.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),

):
    return crud.create_comment(db=db, post=post, user=current_user,comment_type="post", post_id=post_id)

@router.post("/{post_id}/comments/{comment_id}/replies/", response_model=schemas.Comment, status_code=201)
def create_post_comment(
        post: schemas.CommentCreate,
        post_id: int,
        comment_id: int,
        current_user: Annotated[user_schema.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),

):
    return crud.create_comment(db=db, post=post, user=current_user,comment_type="post", comment_id=comment_id)

@router.post("/{post_id}/images", response_model=schemas.PostImage, status_code=201)
def upload_basetisname_post_image(
        image: schemas.PostImageCreate,
        post_id: int,
        current_user: Annotated[user_schema.User, Depends(get_current_active_user)],
        db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.author_id != current_user.username:
        raise HTTPException(status_code=403, detail="You are not the author of this post")
    return crud.upload_post_image(db, image, post_id)