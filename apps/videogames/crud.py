from sqlalchemy.orm import Session

from core import models
from routers.users import schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username,
                          first_name=user.first_name,
                          last_name=user.last_name,
                          email=user.email,
                          password=fake_hashed_password,
                          active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserCreate, username: str):
    db_user = get_user(db, username)
    if db_user is None:
        return None
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db, username):
    db_user = get_user(db, username)
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return True


def change_password(db, username, password):
    db_user = get_user(db, username)
    if db_user is None:
        return None
    db_user.password = password
    db.commit()
    db.refresh(db_user)
    return db_user
