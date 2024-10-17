import json

from storage.istorage import IStorage

FILE_PATH = 'data/movies.json'

class StorageJson(IStorage):
    def list_movies(self):
        """Returns a dictionary of movies stored in the JSON file."""
        try:
            with open(FILE_PATH, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def add_movie(self, title, year, rating, poster):
        """Adds a movie to the JSON file."""
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self.save_movies(movies)

    def delete_movie(self, title):
        """Deletes a movie from the JSON file."""
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)

    def update_movie(self, title, rating):
        """Updates the rating of a movie in the JSON file."""
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self.save_movies(movies)

    def save_movies(self, movies):
        """Saves the movies dictionary back to the JSON file."""
        with open(FILE_PATH, 'w') as file:
            json.dump(movies, file, indent=4)