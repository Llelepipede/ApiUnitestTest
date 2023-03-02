from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from database import Base

class GameDB(Base):
    __tablename__ = 'Games'
    id = Column(Integer, primary_key=True)
    Name = Column(String(100))
    StudioName = Column(String(100))