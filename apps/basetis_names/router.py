from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from . import crud, schemas
from apps.users import schemas as user_schema
from core.database import get_db

router = APIRouter(
    prefix="/basetisnames",
    tags=["basetisnames"],
)


@router.post("/", response_model=schemas.BasetisNamePost, status_code=201)
def create_basetisname_post(
        post: schemas.BasetisNamePostCreate,
        db: Session = Depends(get_db),
        current_user: user_schema.User = Depends(crud.get_current_active_user),
):
    return crud.create_post(db=db, post=post, user=current_user)


@router.get("/", response_model=list[schemas.BasetisNamePost])
def read_basetisname_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_names(db, skip=skip, limit=limit)


@router.get("/{post_id}", response_model=schemas.BasetisNamePost)
def read_basetisname_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/{post_id}", response_model=schemas.BasetisNamePost)
def update_basetisname_post(
        post_id: int, post: schemas.BasetisNamePostCreate, db: Session = Depends(get_db)
):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.update_post(db, post, post_id)


@router.delete("/{post_id}", response_model=schemas.BasetisNamePost)
def delete_basetisname_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.delete_post(db, post_id)


@router.post("/{post_id}/images", response_model=schemas.PostImage, status_code=201)
def upload_basetisname_post_image(
        image: schemas.PostImageCreate,
        post_id: int,
        db: Session = Depends(get_db),
):
    return crud.upload_post_image(db, image, post_id)
