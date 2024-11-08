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



def undo_collections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.collections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM collections"))

    db.session.commit()
