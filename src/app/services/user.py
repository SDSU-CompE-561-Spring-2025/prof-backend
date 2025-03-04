from app.core.config import get_settings
from app.core.security import verify_password
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from app.core.auth import get_password_hash
from app.models.user import User

settings = get_settings()


# User CRUD operations
def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    verification_code = "1234"  # TODO: Implement verification code

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hashed_password,
        verification_code=verification_code,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user
