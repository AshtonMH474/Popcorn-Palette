from app.models import db, Genre, environment, SCHEMA
from sqlalchemy.sql import text

def seed_genres():
    genre1 = Genre(type='action')
    genre2 = Genre(type='romance')
    genre3 = Genre(type='scifi')
    genre4 = Genre(type='comedy')
    genre5 = Genre(type='horror')
    genre6 = Genre(type='superhero')
    genre7 = Genre(type='drama')
    genre8 = Genre(type='documentary')

    genres = [genre1,genre2,genre3,genre4,genre5,genre6,genre7,genre8]
    for genre in genres:
        db.session.add(genre)
    db.session.commit()



def undo_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM genres"))

    db.session.commit()
