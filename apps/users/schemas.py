from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserCreate(UserBase):
    email: str
    password: str


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str | None = None


class User(UserBase):
    email: str
    is_active: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
