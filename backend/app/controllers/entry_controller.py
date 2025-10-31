from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.entry_schema import EntryCreate
from app.services.entry_service import addEntry, getEntry
from app.core.database import get_db

router = APIRouter(prefix="/entries", tags=["Entry"])

@router.post("/add")
def add(entry: EntryCreate, db: Session = Depends(get_db)):
    addEntry(db, entry)
    return{"message": "Entry added successfully"}

@router.get("/get")
def get(userId: int, entryId: int,db: Session = Depends(get_db)):
    return getEntry(db, userId, entryId)