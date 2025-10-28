from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.core.security import hash_password, verify_password, create_access_token
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


def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Create JWT token
    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
