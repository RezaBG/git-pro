import json
from .istorage import IStorage

FILE_NAME = "data/movies.json"

class StorageJson(IStorage):
    def list_movies(self):
        try:
            with open(FILE_NAME, "r") as file:
                movies = json.load(file)
        except FileNotFoundError:
            movies = {}  # Return an empty dictionary if the file is not found
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        if title in movies:
            print(f"Movie {title} already exists!")
            return
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self.save_movies(movies)
        print(f"Added {title} ({year}): {rating}")

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)
            print(f"Movie {title} deleted.")
        else:
            print(f"Movie {title} not found!")

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self.save_movies(movies)
            print(f"Movie {title} updated with new rating {rating}.")
        else:
            print(f"Movie {title} not found!")

    def save_movies(self, movies):
        with open(FILE_NAME, "w") as file:
            json.dump(movies, file, indent=4)