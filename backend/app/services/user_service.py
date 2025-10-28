from datetime import date
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.repositories.user_repository import get_user_by_email, create_user

def register_user(db: Session, email: str, password: str, username: str | None, birthdate: str | None):
    if get_user_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already registered")

    try:
        birthdate_value = date.fromisoformat(birthdate) if birthdate else None
    except ValueError:
        raise HTTPException(status_code=422, detail="birthdate must be YYYY-MM-DD")

    hashed = hash_password(password)
    user = create_user(db, email, hashed, username, birthdate_value)
    return user
