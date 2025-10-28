from sqlalchemy.orm import Session
from app.models.entry_model import Entry
from app.schemas.entry_schema import EntryCreate

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