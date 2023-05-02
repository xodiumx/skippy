import re

from pydantic import BaseModel, Field, validator


class BaseUser(BaseModel):
    email: str = Field(..., min_length=1, max_length=64,)
    username: str = Field(..., min_length=1, max_length=64,)


class UserCreate(BaseUser):
    password: str = Field(..., min_length=8, max_length=64,)

    @validator('email')
    @classmethod
    def validate_email(cls, value):
        if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
            raise ValueError('Email is invalid')
        return value


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'Bearer'
