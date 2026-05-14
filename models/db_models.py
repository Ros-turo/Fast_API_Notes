from database import Base
from sqlalchemy import Column, String,Integer, Boolean

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer,primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_done = Column(Boolean, default=False)