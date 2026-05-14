from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('postgresql://fakturo_user:pass@localhost:5432/notes_db')

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass