from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from datetime import date

from app.core.database import engine
from app.schemas.user import UserRegister
from app.utils.security import hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegister):
    hashed = hash_password(user.password)

    birthdate_value = None
    if user.birthdate:
        try:
            birthdate_value = date.fromisoformat(user.birthdate)
        except ValueError:
            raise HTTPException(status_code=422, detail="birthdate must be YYYY-MM-DD")

    with engine.begin() as conn:
        try:
            conn.execute(
                text("""
                    INSERT INTO users (email, password_hash, username, birthdate)
                    VALUES (:email, :password_hash, :username, :birthdate)
                """),
                {
                    "email": user.email,
                    "password_hash": hashed,
                    "username": user.username,
                    "birthdate": birthdate_value
                }
            )
        except Exception:
            raise HTTPException(status_code=400, detail="Email already registered")

    return {"message": "User created successfully"}
