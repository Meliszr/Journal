from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import isUserReal
from app.repositories.entry_repository import addEntryToDb, getEntryFromDb
from app.schemas.entry_schema import EntryCreate


def addEntry(db: Session, entry: EntryCreate):
    addEntryToDb(db, entry)
    #TODO:
    #error handling
    #check if content is too long
    #check if user exists
    #return something

def getEntry(db: Session, userId: int, entryId: int):

    if(isUserReal(db, userId) == False):
        raise HTTPException(status_code=404, detail=(
            "User not found"
        ))

    entry = getEntryFromDb(db, userId, entryId)
    if(entry == False):
        raise HTTPException(status_code=404, detail=(
            "Entry not found"
        ))
    else:
        return entry

