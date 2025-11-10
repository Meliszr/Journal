from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import isUserReal
from app.repositories.entry_repository import addEntryToDb, getEntryFromDb, getAllEntriesFromDb, deleteEntryFromDb, updateEntryInDb
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

def getAllEntries(db: Session, userId: int):

    if(isUserReal(db, userId) == False):
        raise HTTPException(status_code=404, detail=(
            "User not found"
        ))

    entries = getAllEntriesFromDb(db, userId)
    if (entries == False):
        raise HTTPException(status_code=404, detail=(
            "Entry not found"
        ))
    else:
        return entries

def deleteEntry(db, userId: int, entryId: int):
    if not isUserReal(db, userId):
        raise HTTPException(status_code=404, detail="User not found")

    deleted = deleteEntryFromDb(db, userId, entryId)
    if not deleted:
        raise HTTPException(status_code=404, detail="Entry not found or not authorized to delete")

def update_Entry(db, userId: int, entryId, entry: EntryCreate):

    if not isUserReal(db, userId):
        raise HTTPException(status_code=404, detail="User not found")

    updated = updateEntryInDb(db,userId, entryId, entry)
    if not updated:
        raise HTTPException(status_code=404, detail="Entry not found or not authorized to update")