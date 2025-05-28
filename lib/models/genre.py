from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    movies = relationship("Movie", back_populates="genre")

    def __repr__(self):
        return f"<Genre(name='{self.name}')>"