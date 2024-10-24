from app.models import db, Artist, environment, SCHEMA
from app.models.artist import crew
from sqlalchemy.sql import text


def seed_comedy_movie_artists():
    # Artists for "Superbad"
    superbad_artist1 = Artist(
    first_name='Jonah',
    last_name='Hill',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729738842/JonahHill_fpfpnw.jpg'
    )

    superbad_artist2 = Artist(
    first_name='Michael',
    last_name='Cera',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729738841/MichaelCera_nrxuq5.jpg'
    )

    superbad_artist3 = Artist(
    first_name='Christopher',
    last_name='Mintz-Plasse',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729738837/ChrisMintz_opnvcf.jpg'
    )

    superbad_artist4 = Artist(
    first_name='Bill',
    last_name='Hader',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729738837/BillHader_n52u8y.jpg'
    )

    superbad_artist5 = Artist.query.filter_by(
    first_name='Seth',
    last_name='Rogen',
    ).first()

# Director for "Superbad"
    superbad_director = Artist(
    first_name='Greg',
    last_name='Mottola',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729738838/GregMottola_udygsk.jpg'
    )

# Add artists to the database
    superbad_artists = [superbad_artist1, superbad_artist2, superbad_artist3, superbad_artist4, superbad_artist5,superbad_director]
    for person in superbad_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Superbad"
    superbad_crew1 = crew.insert().values(
    artist_id=superbad_artist1.id,
    movie_id=23,  # Superbad movie ID
    role='Actor',
    played='Seth'
    )

    superbad_crew2 = crew.insert().values(
    artist_id=superbad_artist2.id,
    movie_id=23,
    role='Actor',
    played='Evan'
    )

    superbad_crew3 = crew.insert().values(
    artist_id=superbad_artist3.id,
    movie_id=23,
    role='Actor',
    played='Fogell (McLovin)'
    )

    superbad_crew4 = crew.insert().values(
    artist_id=superbad_artist4.id,
    movie_id=23,
    role='Actor',
    played='Officer Michaels'
    )

    superbad_crew5 = crew.insert().values(
    artist_id=superbad_artist5.id,
    movie_id=23,
    role='Actor',
    played='Officer Slater'
    )

    superbad_crew6 = crew.insert().values(
    artist_id=superbad_director.id,
    movie_id=23,
    role='Director'
    )

# Add crew entries to the database
    superbad_crew = [superbad_crew1, superbad_crew2, superbad_crew3, superbad_crew4, superbad_crew5, superbad_crew6]
    for person in superbad_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "The Hangover"
    hangover_artist1 = Artist(
    first_name='Bradley',
    last_name='Cooper',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739169/Bradley-Cooper-2008.jpg_bavqwz.webp'
    )

    hangover_artist2 = Artist(
    first_name='Ed',
    last_name='Helms',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739178/Ed_Helms_o0soo0.webp'
    )

    hangover_artist3 = Artist(
    first_name='Zach',
    last_name='Galifianakis',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739212/ZachG_rat0hd.jpg'
    )

    hangover_artist4 = Artist(
    first_name='Justin',
    last_name='Bartha',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739224/JustinBaratha_orinl1.jpg'
    )

    hangover_artist5 = Artist(
    first_name='Heather',
    last_name='Graham',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739204/HeatherGraham_drlssg.jpg'
    )

# Director for "The Hangover"
    hangover_director = Artist(
    first_name='Todd',
    last_name='Phillips',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729739239/ToddPhilips_ouwgmn.jpg'
    )

# Add artists to the database
    hangover_artists = [hangover_artist1, hangover_artist2, hangover_artist3, hangover_artist4, hangover_artist5,hangover_director]
    for person in hangover_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The Hangover"
    hangover_crew1 = crew.insert().values(
    artist_id=hangover_artist1.id,
    movie_id=24,  # The Hangover movie ID
    role='Actor',
    played='Phil Wenneck'
    )

    hangover_crew2 = crew.insert().values(
    artist_id=hangover_artist2.id,
    movie_id=24,
    role='Actor',
    played='Stu Price'
    )

    hangover_crew3 = crew.insert().values(
    artist_id=hangover_artist3.id,
    movie_id=24,
    role='Actor',
    played='Alan Garner'
    )

    hangover_crew4 = crew.insert().values(
    artist_id=hangover_artist4.id,
    movie_id=24,
    role='Actor',
    played='Doug Billings'
    )

    hangover_crew5 = crew.insert().values(
    artist_id=hangover_artist5.id,
    movie_id=24,
    role='Actor',
    played='Jade'
    )

    hangover_crew6 = crew.insert().values(
    artist_id=hangover_director.id,
    movie_id=24,
    role='Director'
    )

# Add crew entries to the database
    hangover_crew = [hangover_crew1, hangover_crew2, hangover_crew3, hangover_crew4, hangover_crew5, hangover_crew6]
    for person in hangover_crew:
        db.session.execute(person)
    db.session.commit()

def undo_comedy_movie_artists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.artists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM artists"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.crew RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM crew"))

    db.session.commit()
