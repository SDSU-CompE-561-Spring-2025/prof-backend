from fastapi import FastAPI
from datetime import datetime, UTC

from app.core.database import Base, engine
from sqlalchemy import Column, Integer, Boolean, String, DateTime
from pydantic import BaseModel, EmailStr, Field, constr, field_validator
from app.routes.user import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(user_router, prefix="/auth", tags=["User"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(UTC))


class UserBase(BaseModel):
    username: constr(min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=8, max_length=64)


# TODO: Add custom validator
