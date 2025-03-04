from fastapi import APIRouter
from app.schemas.category import CategoryCreate, CategoryResponse
from app.dependencies import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.auth import oauth2_scheme, decode_access_token
import app.services.category as category_service
import app.services.user as user_service

router = APIRouter()


@router.post("/", response_model=CategoryResponse)
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    username = decode_access_token(token).username
    user = user_service.get_user_by_username(db, username)

    user_id = user.id

    return category_service.create_category(db, category, user_id)
