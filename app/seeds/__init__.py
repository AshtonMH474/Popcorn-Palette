from flask.cli import AppGroup
from .users import seed_users, undo_users
from .movies import seed_movies,undo_movies
from app.models.db import db, environment, SCHEMA
from .movie_images import seed_movie_images,undo_movie_images
from .watchlist import seed_watchlist,undo_watchlist
from.reviews import seed_reviews,undo_reviews
from .genres import seed_genres,undo_genres
from .movie_genres import seed_movie_genres,undo_movie_genres
from .crew.random_movies import seed_random_movie_artists,undo_random_movie_artists
from .crew.recent_movies import seed_recent_movie_artists,undo_recent_movie_artists

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_recent_movie_artists()
        undo_random_movie_artists()
        undo_movie_genres()
        undo_genres()
        undo_reviews()
        undo_watchlist()
        undo_movie_images()
        undo_movies()
        undo_users()

    seed_users()
    seed_movies()
    seed_movie_images()
    seed_watchlist()
    seed_reviews()
    seed_genres()
    seed_movie_genres()
    seed_random_movie_artists()
    seed_recent_movie_artists()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_recent_movie_artists
    undo_random_movie_artists()
    undo_movie_genres()
    undo_genres()
    undo_reviews()
    undo_watchlist()
    undo_movie_images()
    undo_movies()
    undo_users()

    # Add other undo functions here
