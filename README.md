# Top-Movies

This is a web application built with Flask that allows users to add, edit, and delete movie reviews. Users can search for movies, add them to their collection, and review them.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment: `python3 -m venv venv`.
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`.
6. Run the application: `python app.py`.

## Usage

### Home Page
- Upon visiting the home page (`/`), users can view their list of movies with their ratings and reviews.

### Add Movie
- Access the add movie page by visiting `/add`.
- Enter the title of the movie you want to add.
- The application fetches movie details from an external API and displays a list of options.
- Select the desired movie from the list to add it to your collection.

### Edit Movie
- Click on a movie title on the home page to edit its details.
- Users can edit the rating and review of the movie.
- Submit the form to save the changes.

### Delete Movie
- Click on the delete button next to a movie on the home page to remove it from your collection.

## Configuration

- The application uses a secret key for CSRF protection. You can change this key by modifying the `SECRET_KEY` variable in `app.py`.
- The database URI is set to a SQLite database named `mymovies.db`. You can change this in `app.py` by modifying the `SQLALCHEMY_DATABASE_URI` variable.
- Ensure you have set up an environment variable named `MOVIE_API_KEY` containing your API key for accessing movie data from an external API.

## Credits

This project uses Flask, SQLAlchemy, Flask-WTF, Flask-Bootstrap, and requests library.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
