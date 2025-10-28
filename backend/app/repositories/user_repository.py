from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, email: str, password_hash: str, username: str, birthdate):
    user = User(
        email=email,
        password_hash=password_hash,
        username=username,
        birthdate=birthdate
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
