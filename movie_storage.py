import json

FILE_NAME = "movies.json"


def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data. 

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    try:
        with open(FILE_NAME, "r") as file:
            movies = json.load(file)
    except FileNotFoundError:
        movies = {}  # Return an empty dictionary if the file is not found
    return movies


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()  # Load current movies

    if title in movies:
        print(f"Movie {title} already exists!")
        return

    # Add the new movie to the dictionary
    movies[title] = {"year": year, "rating": rating}

    # Save the updated movies dictionary
    save_movies(movies)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()  # Load current movies

    if title in movies:
        del movies[title]  # Delete the movie from the dictionary
        save_movies(movies)  # Save the updated movies dictionary
        print(f"Movie {title} deleted.")
    else:
        print(f"Movie {title} not found!")


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()  # Load current movies

    if title in movies:
        movies[title]["rating"] = rating  # Update the movie's rating
        save_movies(movies)  # Save the updated movies dictionary
        print(f"Movie {title} updated with new rating {rating}.")
    else:
        print(f"Movie {title} not found!")
