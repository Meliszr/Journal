from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.repositories.entry_repository import addEntryToDb
from app.schemas.entry_schema import EntryCreate
from app.services.entry_service import addEntry
from app.core.database import get_db

router = APIRouter(prefix="/entries", tags=["Entry"])

@router.post("/add")
def add(entry: EntryCreate, db: Session = Depends(get_db)):
    addEntry(db, entry)
    return{"message": "Entry added successfully"}
