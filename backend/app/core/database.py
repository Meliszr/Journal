from sqlalchemy import create_engine

DATABASE_URL = "postgresql://localhost/journal_db"
engine = create_engine(DATABASE_URL, echo=False)
