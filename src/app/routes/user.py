from fastapi import APIRouter, Depends

from app.schemas.user import UserResponse, UserCreate
import app.services.user as user_service
from app.dependencies import get_db
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = user_service.create_user(db=db, user=user)
    return new_user


@router.post("/token")
async def login_for_access_token():
    return {"message": "User logged in successfully"}


@router.get("/users/me")
def read_users_me():
    return {"message": "User details returned successfully"}


@router.post("/users/verify-email/{verification_code}")
def verify_email(verification_code: str):
    return {"message": "Email verified successfully"}


def example_func():
    return "Hello from example_func"
