from app.models import db, Collection,Movie, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date



def seed_collections():
    # Create collections
    collection1 = Collection(title='SciFi', description='Science Fiction might be my favorite genre, so why not keep some of my favorites together', user_id=1)
    collection2 = Collection(title='Superhero', description='Batman, Superman, you name it', user_id=1)
    collection3 = Collection(title='Throwbacks', description='Some I love rewatching', user_id=1)

    collections = [collection1, collection2, collection3]

    # Add collections to the session
    for collection in collections:
        db.session.add(collection)
    db.session.commit()

    # Adding to the Superhero collection
    superhero_ids = [155, 335983, 475557, 533535, 580489, 889737, 912649]
    superheros = [Movie.query.filter_by(id=movie_id).first() for movie_id in superhero_ids]

    # Only append valid movies (non-None)
    for superhero in superheros:
        if superhero:  # Make sure the movie exists
            collection2.movies.append(superhero)
        else:
            print(f"Superhero movie with id {superhero_ids[superheros.index(superhero)]} not found.")

    # Adding to the SciFi collection
    sci_fi_ids = [11, 698687, 945961, 198663]
    sci_fis = [Movie.query.filter_by(id=movie_id).first() for movie_id in sci_fi_ids]

    # Only append valid movies (non-None)
    for sci in sci_fis:
        if sci:  # Make sure the movie exists
            collection1.movies.append(sci)
        else:
            print(f"SciFi movie with id {sci_fi_ids[sci_fis.index(sci)]} not found.")

    # Adding to the Throwback collection
    throwback_ids = [11, 64688, 4951, 447332, 155]
    throwbacks = [Movie.query.filter_by(id=movie_id).first() for movie_id in throwback_ids]

    # Only append valid movies (non-None)
    for throw in throwbacks:
        if throw:  # Make sure the movie exists
            collection3.movies.append(throw)
        else:
            print(f"Throwback movie with id {throwback_ids[throwbacks.index(throw)]} not found.")

    # Commit changes
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
