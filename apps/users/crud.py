from passlib.context import CryptContext
from sqlalchemy.orm import Session

from core import models
from apps.users import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username,
                          first_name=user.first_name,
                          last_name=user.last_name,
                          email=user.email,
                          password=fake_hashed_password,
                          is_active=True)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user: schemas.UserUpdate, username: str):
    db_user = get_user(db, username)
    if db_user is None or not db_user.is_active:
        return None
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db, username):
    db_user = get_user(db, username)
    if db_user is None or not db_user.is_active:
        return None
    db_user.is_active = False
    db.commit()
    return True


def change_password(db, username, password):
    db_user = get_user(db, username)
    if db_user is None or not db_user.is_active:
        return None
    db_user.password = get_password_hash(password)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)