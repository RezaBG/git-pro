# main.py
import requests
from storage.storage_json import StorageJson

# Using your OMDb API key
OMDB_API_KEY = "7428de20"  # Your API key

class MovieApp:
    def __init__(self, storage):
        self.storage = storage

    def list_movies(self):
        movies = self.storage.list_movies()
        if not movies:
            print("No movies in database.")
        else:
            print(f"{len(movies)} movies in database:")
            for title, info in movies.items():
                print(f" - {title} ({info['year']}): {info['rating']}")

    def add_movie(self):
        title = input("Enter movie title: ").strip()
        movie_data = self.fetch_movie_data(title)

        if movie_data:
            year = movie_data.get("Year", "N/A")
            rating = float(movie_data.get("imdbRating", 0)) if movie_data.get("imdbRating") != "N/A" else 0
            poster = movie_data.get("Poster", "")
            self.storage.add_movie(title, year, rating, poster)
        else:
            print(f"Movie '{title}' not found!")

    def fetch_movie_data(self, title):
        """Fetch movie data from OMDb API."""
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data.get("Response") == "True":
                return data
            else:
                print(f"Error: {data.get('Error')}")
                return None
        except requests.RequestException as e:
            print(f"Error fetching movie data: {e}")
            return None

    def delete_movie(self):
        title = input("Enter movie title: ")
        self.storage.delete_movie(title)

    def update_movie(self):
        title = input("Enter movie title: ")
        rating = float(input("Enter new movie rating: "))
        self.storage.update_movie(title, rating)

    def generate_website(self):
        """Generates an HTML website for the movie collection."""
        try:
            # Read the template file
            with open('static/index_template.html', 'r') as template_file:
                template_content = template_file.read()

            # Replace the title placeholder
            template_content = template_content.replace("__TEMPLATE_TITLE__", "My Movie App")

            # Generate the movie grid HTML
            movies = self.storage.list_movies()
            movie_grid_html = ""
            for title, info in movies.items():
                movie_grid_html += f"""
                <div class="movie">
                    <h2>{title}</h2>
                    <p>{info['year']} - Rating: {info['rating']}</p>
                    <img src="{info['poster']}" alt="{title} poster">
                </div>
                """

            # Replace the movie grid placeholder
            template_content = template_content.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)

            # Write the generated HTML to the index.html file
            with open('index.html', 'w') as output_file:
                output_file.write(template_content)

            print("Website generated successfully.")

        except FileNotFoundError:
            print("Error: Template file not found.")

    def run(self):
        while True:
            print("***** My Movie Database *****")
            print("0. Exit")
            print("1. List all movies")
            print("2. Add a movie")
            print("3. Delete a movie")
            print("4. Update a movie")
            print("5. Generate website")  # New option for generating the website
            choice = input("Enter choice (0-5): ")
            if choice == "0":
                break
            elif choice == "1":
                self.list_movies()
            elif choice == "2":
                self.add_movie()
            elif choice == "3":
                self.delete_movie()
            elif choice == "4":
                self.update_movie()
            elif choice == "5":
                self.generate_website()  # Call the generate website function
            else:
                print("Invalid choice")

if __name__ == "__main__":
    storage = StorageJson()  # You can later switch to StorageCsv if needed
    app = MovieApp(storage)
    app.run()