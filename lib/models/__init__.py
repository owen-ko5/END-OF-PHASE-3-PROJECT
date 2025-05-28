from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///movies.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from .movie import Movie
from .genre import Genre

Base.metadata.create_all(engine)