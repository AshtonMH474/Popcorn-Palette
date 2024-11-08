from flask.cli import AppGroup
from .users import seed_users, undo_users
from .movies import undo_movies
from app.models.db import db, environment, SCHEMA
from .movie_images import undo_movie_images
from .watchlist import seed_watchlist,undo_watchlist
from.reviews import seed_reviews,undo_reviews
from .genres import undo_genres
from .movie_genres import undo_movie_genres
from .movies_api import seed_api_movies
from .collections import seed_collections,undo_collections
from .collection_movies import seed_collection_movies,undo_collection_movies
# from .crew.random_movies import seed_random_movie_artists,undo_random_movie_artists
# from .crew.recent_movies import seed_recent_movie_artists,undo_recent_movie_artists
# from .crew.comedies import seed_comedy_movie_artists,undo_comedy_movie_artists
# from .crew.horrores import seed_horror_movie_artists,undo_horror_movie_artists

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
        undo_collection_movies()
        undo_collections()
        undo_movie_genres()
        undo_genres()
        undo_reviews()
        undo_watchlist()
        undo_movie_images()
        undo_movies()
        undo_users()

    seed_users()
    seed_api_movies()
    seed_watchlist()
    seed_reviews()
    seed_collections()
    seed_collection_movies()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_collection_movies()
    undo_collections()
    undo_movie_genres()
    undo_genres()
    undo_reviews()
    undo_watchlist()
    undo_movie_images()
    undo_movies()
    undo_users()

    # Add other undo functions here
