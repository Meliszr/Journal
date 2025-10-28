from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app.repositories.entry_repository import addEntryToDb
from app.schemas.entry_schema import EntryCreate


def addEntry(db: Session, entry: EntryCreate):
    addEntryToDb(db, entry)