from app.models import db, Movie,User, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


def seed_watchlist():
    demo = User.query.filter_by(email='demo@aa.io').first()
    # movie1 = Movie.query.filter_by(title='Transformers: One').first()
    # movie2 = Movie.query.filter_by(title='Star Wars: Episode IV - A New Hope').first()
    # movie3 = Movie.query.filter_by(title='The Dark Knight').first()
    # movie4 = Movie.query.filter_by(title='10 Things I Hate About You').first()
    # movie5 = Movie.query.filter_by(title='A Quiet Place').first()
    # movie6 = Movie.query.filter_by(title='21 Jump Street').first()
    # movie7 = Movie.query.filter_by(title='Bob Marley: One Love').first()
    # movie8 = Movie.query.filter_by(title='Oppenheimer').first()

    # demo.watchlist_movies.append(movie1)
    # demo.watchlist_movies.append(movie2)
    # demo.watchlist_movies.append(movie3)
    # demo.watchlist_movies.append(movie4)
    # demo.watchlist_movies.append(movie5)
    # demo.watchlist_movies.append(movie6)
    # demo.watchlist_movies.append(movie7)
    # demo.watchlist_movies.append(movie8)

    movie_ids = [
        {'id':698687,
         'title':'Transformers: One',
         'release_date':date(2024,9,20),
         'custom':False

        },
        {
        'id':11,
        'title':'Star Wars: Episode IV - A New Hope',
        'release_date':date(1977,5,25),
        'custom':False
            },
            {
        'id':155,
        'title':'The Dark Knight',
        'release_date':date(2008,7,18),
        'custom':False
         },
                 {
        'id':4951,
        'title':'10 Things I Hate About You',
        'release_date':date(1999,3,31),
        'custom':False
                     },
                     {
        'id':447332,
        'title':'A Quiet Place',
        'release_date':date(2018,4,6),
        'custom':False
                     },
                     {
        'id':64688,
        'title':'21 Jump Street',
        'release_date':date(2012,3,16),
        'custom':False
                     },
                     {
        'id':802219,
        'title':'Bob Marley: One Love',
        'release_date':date(2024,2,14),
        'custom':False
                     },
                     {
        'id':857,
        'title':'Saving Private Ryan',
        'release_date':date(1998,7,24),
        'custom':False
                     }
                     ]  # Replace with actual movie IDs

# Loop through the movie IDs and append them directly
    for movie in movie_ids:
        new_movie=Movie(id=movie['id'],title=movie['title'],release_date=movie['release_date'],custom=movie['custom'])
        demo.watchlist_movies.append(new_movie)
        db.session.add(new_movie)
    db.session.commit()
def undo_watchlist():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.watchlist RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM watchlist"))
        db.session.execute(text("DELETE FROM movies"))

    db.session.commit()
