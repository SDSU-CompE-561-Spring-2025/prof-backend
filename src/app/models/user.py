from sqlalchemy import Column, Integer, Boolean, String, DateTime
from datetime import datetime, UTC
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=True)
    verification_code = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now(UTC))

    # TODO: Add relations to transactions and categories
