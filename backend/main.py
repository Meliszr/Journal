from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from datetime import date
from sqlalchemy import create_engine, text
from auth import hash_password  # your hash functions

DATABASE_URL = "postgresql://localhost/journal_db"
engine = create_engine(DATABASE_URL)

app = FastAPI()


class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: str | None = None
    birthdate: str | None = None  # ⬅️ Now stored as string, not date

    @field_validator("birthdate", mode="before")
    def clean_birthdate(cls, v):
        # Swagger sends "string" when field is blank → ignore it
        if v in (None, "", "string"):
            return None
        return v

@app.post("/register")
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

