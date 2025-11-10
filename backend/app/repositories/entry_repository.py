from datetime import datetime
from sqlalchemy.orm import Session
from app.models.entry_model import Entry
from app.schemas.entry_schema import EntryCreate
from zoneinfo import ZoneInfo

#from app.models. import User

def addEntryToDb(db: Session, entry: EntryCreate):
    entrySecure = Entry(
        title=entry.title,
        content=entry.content,
        user_id=entry.userId,
    )

    db.add(entrySecure)
    db.commit()
    db.refresh(entrySecure)
    return entrySecure

def getEntryFromDb(db: Session, userId: int, entryId: int):
    return db.query(Entry).filter(Entry.id == entryId, Entry.user_id == userId,
                                  Entry.is_deleted == False).first()

def getAllEntriesFromDb(db: Session, userId: int):
    return db.query(Entry).filter(Entry.user_id == userId, Entry.is_deleted == False).all()

def deleteEntryFromDb(db, userId: int, entryId: int):
    entry = db.query(Entry).filter(
        Entry.id == entryId,
        Entry.user_id == userId,
        Entry.is_deleted == False
    ).first()

    if not entry:
        return False

    # Soft delete
    entry.is_deleted = True
    db.commit()
    return True

def updateEntryInDb(db: Session, userId: int, entryId: int, entry: EntryCreate):
    entrySecure = db.query(Entry).filter(
        Entry.id == entryId,
        Entry.user_id == userId,
        Entry.is_deleted == False
    ).first()

    if not entrySecure:
        return None

    entrySecure.title = entry.title
    entrySecure.content = entry.content
    entrySecure.updated_at = datetime.now(ZoneInfo("Europe/Vienna")) #change later to utc or something

    db.commit()
    db.refresh(entrySecure)
    return entrySecure