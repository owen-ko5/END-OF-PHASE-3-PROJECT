from lib.helper import create_movie, list_movies, delete_movie, list_genres

def main():
    print("Welcome to Movie Tracker CLI")
    while True:
        print("\nOptions: [1] Add Movie [2] List Movies [3] Delete Movie [4] List Genres [0] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Movie Title: ")
            year = int(input("Release Year: "))
            genre = input("Genre: ")
            movie = create_movie(title, year, genre)
            print(f"Added: {movie}")
        elif choice == '2':
            for movie in list_movies():
                print(movie)
        elif choice == '3':
            title = input("Title of movie to delete: ")
            success = delete_movie(title)
            print("Deleted." if success else "Movie not found.")
        elif choice == '4':
            for genre in list_genres():
                print(genre)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")