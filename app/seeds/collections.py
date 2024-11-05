from app.models import db, Collection,Movie, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date



def seed_collections():
    collection1 = Collection(title='SciFi',description='Science Fiction might be my favorite gerne so why not keep some of my favoirtes togteher',user_id=1)
    collection2 = Collection(title='Superhero',description='Batman Superman you name it',user_id=1)
    collection3 = Collection(title='Throwbacks',description='Some I love rewatching',user_id=1)

    collections = [collection1,collection2,collection3]

    for collection in collections:
        db.session.add(collection)
    db.session.commit()

    # adding to SuperHero
    superhero1 = Movie.query.filter_by(id=155).first()
    superhero2 = Movie.query.filter_by(id=335983).first()
    superhero3 = Movie.query.filter_by(id=475557).first()
    superhero4 = Movie.query.filter_by(id=533535).first()
    superhero5 = Movie.query.filter_by(id=580489).first()
    superhero6 = Movie.query.filter_by(id=889737).first()
    superhero7 = Movie.query.filter_by(id=912649).first()

    superheros = [superhero1,superhero2,superhero3,superhero4,superhero5,superhero6,superhero7]
    for superhero in superheros:
        collection2.movies.append(superhero)



    # throwbacks

    throw1 = Movie.query.filter_by(id=11).first()
    throw2 = Movie.query.filter_by(id=64688).first()
    throw3 = Movie.query.filter_by(id=4951).first()
    throw4 = Movie.query.filter_by(id=447332).first()
    throw5 = Movie.query.filter_by(id=155).first()


    throwbacks = [throw1,throw2,throw3,throw4,throw5]

    for throw in throwbacks:
        collection3.movies.append(throw)


    db.session.commit()


def undo_collections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collections"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collection_movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collection_movies"))

    db.session.commit()
