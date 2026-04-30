from backend.database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    title = Column(String)
    category = Column(String)
    did_it = Column(Boolean)
    notes = Column(String, nullable=True)
