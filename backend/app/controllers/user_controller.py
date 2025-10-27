from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserRegister
from app.services.user_service import register_user
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    register_user(db, user.email, user.password, user.username, user.birthdate)
    return {"message": "User created successfully"}
