from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserRegister, UserLogin, TokenResponse
from app.services.user_service import register_user, login_user
from app.core.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    register_user(db, user.email, user.password, user.username, user.birthdate)
    return {"message": "User created successfully"}


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_user(db, form_data.username, form_data.password)
