from datetime import datetime
from pydantic import BaseModel, constr, EmailStr, Field


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=8, max_length=64)


# TODO: Add custom validator


class User(UserBase):
    id: int = Field(..., gt=0)
    username: constr(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int = Field(..., gt=0)
    username: constr(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True
