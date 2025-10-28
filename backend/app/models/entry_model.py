from xmlrpc.client import Boolean, DateTime

from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    content = Column(String, nullable=False)
    user_id = Column(Integer, nullable=False)