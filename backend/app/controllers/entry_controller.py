from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.schemas.entry_schema import EntryCreate
from app.services.entry_service import addEntry, getEntry, getAllEntries, deleteEntry
from app.core.database import get_db

router = APIRouter(prefix="/entries", tags=["Entry"])

@router.post("/add")
def add(entry: EntryCreate, db: Session = Depends(get_db)):
    addEntry(db, entry)
    return{"message": "Entry added successfully"}

@router.get("/get")
def get(userId: int, entryId: int,db: Session = Depends(get_db)):
    return getEntry(db, userId, entryId)

@router.get("/get/all")
def getAll(userId: int, db: Session = Depends(get_db)):
    return getAllEntries(db, userId);

@router.delete("/delete/{entry_id}")
def delete_entry(entry_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    deleteEntry(db, user.id, entry_id)
    return {"message": "Entry deleted successfully"}