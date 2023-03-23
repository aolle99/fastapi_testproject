from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import APIRouter
from . import crud, schemas
from apps.users import schemas as user_schema
from core.database import get_db
from ..users.router import get_current_active_user

router = APIRouter(
    prefix="/videogames",
    tags=["videogames"],
)


@router.post("/", response_model=schemas.VideogamePost, status_code=201)
def create_videgame_post(post: schemas.VideogamePostCreate,
                         current_user: Annotated[user_schema.User, Depends(get_current_active_user)]
                         , db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post, user=current_user)


@router.get("/", response_model=list[schemas.VideogamePost])
def read_videgame_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_videogameposts(db, skip=skip, limit=limit)


@router.get("/{post_id}", response_model=schemas.VideogamePost)
def read_videgame_post(post_id: int, db: Session = Depends(get_db)):
    vgp = crud.get_videogamepost(db, post_id=post_id)
    return vgp


@router.get("/videogames/", response_model=list[schemas.Videogame])
def read_videogames(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_videogames(db, skip=skip, limit=limit)


@router.get("/platforms/", response_model=list[schemas.Platform])
def read_platform(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_platforms(db, skip=skip, limit=limit)


@router.get("/genres/", response_model=list[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_genres(db, skip=skip, limit=limit)
