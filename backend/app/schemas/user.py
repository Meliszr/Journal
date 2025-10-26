from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    username: Optional[str] = None
    birthdate: Optional[str] = None

    @field_validator("birthdate", mode="before")
    def clean_birthdate(cls, v):
        if v in (None, "", "string"):
            return None
        return v
