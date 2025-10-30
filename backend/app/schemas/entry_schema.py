import datetime

from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional

class EntryCreate(BaseModel):
    title: Optional[str] = None
    content: str
    userId: int


