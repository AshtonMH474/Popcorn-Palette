from app.models import db, Movie,User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


def seed_watchlist():
    demo = User.query.filter_by(email='demo@aa.io').first()
    movie1 = Movie.query.filter_by(title='Transformers One').first()
    movie2 = Movie.query.filter_by(title='Star Wars').first()
    movie3 = Movie.query.filter_by(title='The Dark Knight').first()
    movie4 = Movie.query.filter_by(title='10 Things I Hate About You').first()
    movie5 = Movie.query.filter_by(title='A Quiet Place').first()
    movie6 = Movie.query.filter_by(title='21 Jump Street').first()
    movie7 = Movie.query.filter_by(title='Bob Marley: One Love').first()
    movie8 = Movie.query.filter_by(title='Oppenheimer').first()

    demo.watchlist_movies.append(movie1)
    demo.watchlist_movies.append(movie2)
    demo.watchlist_movies.append(movie3)
    demo.watchlist_movies.append(movie4)
    demo.watchlist_movies.append(movie5)
    demo.watchlist_movies.append(movie6)
    demo.watchlist_movies.append(movie7)
    demo.watchlist_movies.append(movie8)
    db.session.commit()
def undo_watchlist():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.watchlist RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM watchlist"))

    db.session.commit()
