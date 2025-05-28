from lib.helper import create_movie

sample_data = [
    ("Inception", 2010, "Sci-Fi"),
    ("Titanic", 1997, "Romance"),
    ("The Matrix", 1999, "Sci-Fi"),
    ("The Godfather", 1972, "Crime")
]

for title, year, genre in sample_data:
    create_movie(title, year, genre)

print("Database seeded!")