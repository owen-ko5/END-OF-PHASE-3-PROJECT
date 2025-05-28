from lib.models import session, Movie, Genre

def create_genre(name):
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    return genre

def create_movie(title, year, genre_name):
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = create_genre(genre_name)
    movie = Movie(title=title, year=year, genre=genre)
    session.add(movie)
    session.commit()
    return movie

def list_movies():
    return session.query(Movie).all()

def list_genres():
    return session.query(Genre).all()

def delete_movie(title):
    movie = session.query(Movie).filter_by(title=title).first()
    if movie:
        session.delete(movie)
        session.commit()
        return True
    return False
