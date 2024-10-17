import csv
from storage.istorage import IStorage

class StorageCsv(IStorage):
    FILE_NAME = 'data/movies.csv'

    def list_movies(self):
        movies = {}
        try:
            with open(self.FILE_NAME, newline='', mode='r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    movies[row['title']] = {
                        'year': int(row['year']),
                        'rating': float(row['rating']),
                        'poster': row['poster']
                    }
        except FileNotFoundError:
            print("CSV file not found. Returning empty movie list.")
        return movies

    def add_movie(self, title, year, rating, poster):
        with open(self.FILE_NAME, mode='a', newline='') as csvfile:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'title': title, 'year': year, 'rating': rating, 'poster': poster})

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_all_movies(movies)
        else:
            print(f"Movie '{title}' not found!")

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_all_movies(movies)
        else:
            print(f"Movie '{title}' not found!")

    def _save_all_movies(self, movies):
        with open(self.FILE_NAME, mode='w', newline='') as csvfile:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for title, info in movies.items():
                writer.writerow({
                    'title': title,
                    'year': info['year'],
                    'rating': info['rating'],
                    'poster': info['poster']
                })