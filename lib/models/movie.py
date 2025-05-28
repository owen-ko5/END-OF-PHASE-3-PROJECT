from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genres.id'))

    genre = relationship("Genre", back_populates="movies")

    def __repr__(self):
        return f"<Movie(title='{self.title}', year={self.year}, genre='{self.genre.name}')>"

