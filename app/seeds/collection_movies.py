from app.models import db, Collection,Movie, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date


def seed_collection_movies():
    collection2 = Collection.query.filter_by(id=2).first()
    collection1 = Collection.query.filter_by(id=1).first()

    superhero1 = Movie.query.filter_by(title='The Dark Knight').first()
    superhero3 = Movie.query.filter_by(title='Venom: Let There Be Carnage').first()
    superhero4 = Movie.query.filter_by(title='Deadpool & Wolverine').first()
    superhero5 = Movie.query.filter_by(title='Joker: Folie à Deux').first()
    superhero6 = Movie.query.filter_by(title='Venom: The Last Dance').first()
    superhero7 = Movie.query.filter_by(title='Venom').first()



    collection2.movies.append(superhero1)

    collection2.movies.append(superhero3)
    collection2.movies.append(superhero4)
    collection2.movies.append(superhero5)
    collection2.movies.append(superhero6)
    collection2.movies.append(superhero7)

    db.session.commit()

    sci1 = Movie.query.filter_by(title='Transformers One').first()
    sci2 = Movie.query.filter_by(title='Star Wars').first()

    collection1.movies.append(sci1)
    collection1.movies.append(sci2)

    db.session.commit()



def undo_collection_movies():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collection_movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collection_movies"))

    db.session.commit()
