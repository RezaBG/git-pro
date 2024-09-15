import movie_storage


def display_menu():
    print("***** My Movie Database *****")
    print("0. Exit")
    print("1. List all movies")
    print("2. Add a movie")
    print("3. Delete a movie")
    print("4. Update a movie")
    print("5. Stats")
    print("6. Random movies")
    print("7. Search movies")
    print("8. Movie sort by rating")
    print("9. Movie sort by year")
    print("10. Filter movie")


def list_movies():
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies in database.")
    else:
        print(f"{len(movies)} movies in database: ")
        for title, info in movies.items():
            print(f" - {title} ({info['year']}): {info['rating']}")


def add_movie():
    title = input("Enter movie title: ")
    year = int(input("Enter movie year: "))
    rating = float(input("Enter movie rating: "))
    movie_storage.add_movie(title, year, rating)
    print(f"Added {title} ({year}): {rating}")


def delete_movie():
    title = input("Enter movie title: ")
    movie_storage.delete_movie(title)


def update_movie():
    title = input("Enter movie title: ")
    rating = float(input("Enter new movie rating: "))
    movie_storage.update_movie(title, rating)


def stats_movie():
    movies = movie_storage.get_movies()
    if len(movies) == 0:
        print("No movies in database")
        return

    print("Movie stats:")
    average_rating = sum(info["rating"]
                         for info in movies.values()) / len(movies)
    sorted_ratings = sorted(info["rating"] for info in movies.values())
    mid = len(sorted_ratings) // 2

    if len(sorted_ratings) % 2 == 0:
        median_rating = (sorted_ratings[mid - 1] + sorted_ratings[mid]) / 2
    else:
        median_rating = sorted_ratings[mid]

    best_movie = max(movies.items(), key=lambda item: item[1]["rating"])
    worst_movie = min(movies.items(), key=lambda item: item[1]["rating"])

    print(f"Average rating: {average_rating:.2f}")
    print(f"Median rating: {median_rating:.2f}")
    print(
        f"Best movie: {best_movie[0]} ({best_movie[1]['year']}): {best_movie[1]['rating']}"
    )
    print(
        f"Worst movie: {worst_movie[0]} ({worst_movie[1]['year']}): {worst_movie[1]['rating']}"
    )


def random_movie():
    import random
    movies = movie_storage.get_movies()
    if len(movies) == 0:
        print("No movies in database")
        return

    title, info = random.choice(list(movies.items()))
    print(f"Random movie: {title} ({info['year']}): {info['rating']}")


def search_movie():
    title = input("Enter movie title or part of it: ").strip()
    movies = movie_storage.get_movies()
    found_movies = [
        movie_title for movie_title, info in movies.items()
        if title.lower() in movie_title.lower()
    ]

    if found_movies:
        print(f"Found {len(found_movies)} movies:")
        for movie_title in found_movies:
            info = movies[movie_title]
            print(f" - {movie_title} ({info['year']}): {info['rating']}")
    else:
        print(f"No movies found with title containing '{title}'")


def movie_sort_by_rating():
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(),
                           key=lambda item: item[1]["rating"],
                           reverse=True)
    print("Movies sorted by rating:")
    for title, info in sorted_movies:
        print(f" - {title} ({info['year']}): {info['rating']}")


def movie_sort_by_year():
    latest_first = input(
        "Do you want the latest movies first? (Y/N) ").strip().upper() == "Y"
    movies = movie_storage.get_movies()
    sorted_movies = sorted(movies.items(),
                           key=lambda item: item[1]["year"],
                           reverse=latest_first)
    print("Movies sorted by year:")
    for title, info in sorted_movies:
        print(f" - {title} ({info['year']}): {info['rating']}")


def filter_movie():
    min_rating = input(
        "Enter minimum rating (leave blank for no minimum rating): ").strip()
    start_year = input(
        "Enter start year (leave blank for no start year): ").strip()
    end_year = input("Enter end year (leave blank for no end year): ").strip()

    min_rating = float(min_rating) if min_rating else None
    start_year = int(start_year) if start_year else None
    end_year = int(end_year) if end_year else None

    movies = movie_storage.get_movies()
    filtered_movies = [
        (title, info) for title, info in movies.items()
        if (min_rating is None or info['rating'] >= min_rating) and (
            start_year is None or info['year'] >= start_year) and (
                end_year is None or info['year'] <= end_year)
    ]

    if filtered_movies:
        print(f"Found {len(filtered_movies)} movies:")
        for title, info in filtered_movies:
            print(f" - {title} ({info['year']}): {info['rating']}")
    else:
        print("No movies found matching the criteria.")


def main():
    while True:
        display_menu()
        choice = input("Enter choice (0-10): ")
        if choice == "0":
            break
        elif choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            stats_movie()
        elif choice == "6":
            random_movie()
        elif choice == "7":
            search_movie()
        elif choice == "8":
            movie_sort_by_rating()
        elif choice == "9":
            movie_sort_by_year()
        elif choice == "10":
            filter_movie()
        else:
            print("Invalid choice")
        input("Press enter to continue ")


if __name__ == "__main__":
    main()
