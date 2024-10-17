
# Movie App Project

## Description
The Movie App is a Python-based CLI (Command Line Interface) application that allows users to:
- Add movies to a collection using the OMDb API.
- List, delete, and update movies stored in JSON format.
- Generate a website that displays the movie collection with details like title, year, rating, and movie poster.

The app uses object-oriented programming (OOP) principles and supports multiple storage options (JSON and CSV). It also integrates with the OMDb API to fetch movie data automatically.

## Features
- **CRUD Operations**: Add, list, update, and delete movies.
- **API Integration**: Automatically fetches movie information from the OMDb API using only the movie title.
- **Website Generation**: Generates a static HTML website displaying the movie collection.
- **Multiple Storage Options**: Supports both JSON and CSV storage formats.
- **Error Handling**: Handles common errors like missing movie titles and connection failures.

## Project Structure
```
movie-project/
│
├── data/
│   └── movies.json                # Stores movie data in JSON format
│
├── static/
│   ├── index_template.html         # HTML template for website generation
│   └── style.css                   # Styling for the generated website
│
├── storage/
│   ├── __init__.py
│   ├── istorage.py                 # Interface for storage classes
│   ├── storage_csv.py              # CSV storage implementation
│   └── storage_json.py             # JSON storage implementation
│
├── .gitignore                      # Files to ignore in Git
├── README.md                       # Project information
├── main.py                         # Main application script
├── movies.py                       # Utility functions for movies
└── requirements.txt                # Dependencies list
```

## Requirements
To run this project, you'll need:
- Python 3.x
- The `requests` library (for API integration)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/RezaBG/movie-project
   cd movie-project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Get an OMDb API key:
   - Go to the [OMDb API website](https://www.omdbapi.com/apikey.aspx) and request a free API key.
   - Replace the placeholder `"your_api_key"` in `main.py` with your actual API key.

4. Run the app:
   ```bash
   python main.py
   ```

## Usage
Once the application is running, you can:
- Add a movie using the movie title.
- Generate a website to display your collection.
- List, update, or delete movies from the collection.

## License
This project is licensed under the MIT License.
