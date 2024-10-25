from app.models import db, Artist, environment, SCHEMA
from app.models.artist import crew
from sqlalchemy.sql import text

def seed_horror_movie_artists():
    # Artists for "Hereditary"
    hereditary_artist1 = Artist(
    first_name='Toni',
    last_name='Collette',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814834/ToniCollette_h2qwo8.jpg'
    )

    hereditary_artist2 = Artist(
    first_name='Alex',
    last_name='Wolff',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814791/AlexWolff_t7z6o6.jpg'
    )

    hereditary_artist3 = Artist(
    first_name='Millie',
    last_name='Shapiro',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814813/MillioShapiro_xsuqkm.jpg'
    )

    hereditary_artist4 = Artist(
    first_name='Gabriel',
    last_name='Byrne',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814803/GabrielByrne_jb4vc0.jpg'
    )

    hereditary_artist5 = Artist(
    first_name='Anne',
    last_name='Dowd',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814794/AnnDowd_vcqmdq.jpg'
    )

# Director for "Hereditary"
    hereditary_director = Artist(
    first_name='Ari',
    last_name='Aster',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814798/AriAster_c5cnxh.webp'
    )

# Add artists to the database
    hereditary_artists = [hereditary_artist1, hereditary_artist2, hereditary_artist3, hereditary_artist4, hereditary_artist5,hereditary_director]
    for person in hereditary_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Hereditary"
    hereditary_crew1 = crew.insert().values(
    artist_id=hereditary_artist1.id,
    movie_id=33,  # Hereditary movie ID
    role='Actor',
    played='Annie Graham'
    )

    hereditary_crew2 = crew.insert().values(
    artist_id=hereditary_artist2.id,
    movie_id=33,
    role='Actor',
    played='Peter Graham'
    )

    hereditary_crew3 = crew.insert().values(
    artist_id=hereditary_artist3.id,
    movie_id=33,
    role='Actor',
    played='Charlie Graham'
    )

    hereditary_crew4 = crew.insert().values(
    artist_id=hereditary_artist4.id,
    movie_id=33,
    role='Actor',
    played='Steve'
    )

    hereditary_crew5 = crew.insert().values(
    artist_id=hereditary_artist5.id,
    movie_id=33,
    role='Actor',
    played='Joan'
    )

    hereditary_crew6 = crew.insert().values(
    artist_id=hereditary_director.id,
    movie_id=33,
    role='Director'
    )

# Add crew entries to the database
    hereditary_crew = [hereditary_crew1, hereditary_crew2, hereditary_crew3, hereditary_crew4, hereditary_crew5, hereditary_crew6]
    for person in hereditary_crew:
        db.session.execute(person)
    db.session.commit()


# Artists for "Get Out"
    get_out_artist1 = Artist(
    first_name='Daniel',
    last_name='Kaluuya',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729815786/DanielK_pml4re.avif'
    )

    get_out_artist2 = Artist(
    first_name='Allison',
    last_name='Williams',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729815799/Allison_Williams__2015_sej5oa.png'
    )

    get_out_artist3 = Artist.query.filter_by(
    first_name='Catherine',
    last_name='Keener'
    ).first()

    get_out_artist4 = Artist(
    first_name='Bradley',
    last_name='Whitford',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729815792/BradleuWhitford_ar31qs.jpg'
    )

    get_out_artist5 = Artist(
    first_name='LilRel',
    last_name='Howery',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729815782/Lil_Rel_Howery_dgmqmi.webp'
    )

# Director for "Get Out"
    get_out_director = Artist(
    first_name='Jordan',
    last_name='Peele',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729815778/JordanPeele_ojiuop.jpg'
    )

# Add artists to the database
    get_out_artists = [get_out_artist1, get_out_artist2, get_out_artist4, get_out_artist5,get_out_director]
    for person in get_out_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Get Out"
    get_out_crew1 = crew.insert().values(
    artist_id=get_out_artist1.id,
    movie_id=34,  # Get Out movie ID
    role='Actor',
    played='Chris Washington'
    )

    get_out_crew2 = crew.insert().values(
    artist_id=get_out_artist2.id,
    movie_id=34,
    role='Actor',
    played='Rose Armitage'
    )

    get_out_crew3 = crew.insert().values(
    artist_id=get_out_artist3.id,
    movie_id=34,
    role='Actor',
    played='Missy Armitage'
    )

    get_out_crew4 = crew.insert().values(
    artist_id=get_out_artist4.id,
    movie_id=34,
    role='Actor',
    played='Dean Armitage'
    )

    get_out_crew5 = crew.insert().values(
    artist_id=get_out_artist5.id,
    movie_id=34,
    role='Actor',
    played='Rod Williams'
    )

    get_out_crew6 = crew.insert().values(
    artist_id=get_out_director.id,
    movie_id=34,
    role='Director'
    )

# Add crew entries to the database
    get_out_crew = [get_out_crew1, get_out_crew2, get_out_crew3, get_out_crew4, get_out_crew5, get_out_crew6]
    for person in get_out_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "A Quiet Place"
    quiet_place_artist1 = Artist.query.filter_by(
    first_name='Emily',
    last_name='Blunt',
    ).first()

    quiet_place_artist2 = Artist(
    first_name='John',
    last_name='Krasinski',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816211/JohnKrasinski_mgjjtq.jpg'
    )

    quiet_place_artist3 = Artist(
    first_name='Millicent',
    last_name='Simmonds',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816226/MillicentSimmonds_fznddc.webp'
    )

    quiet_place_artist4 = Artist(
    first_name='Noah',
    last_name='Jupe',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816219/NoahJupe_ybnfva.jpg'
    )

    quiet_place_artist5 = Artist.query.filter_by(
    first_name='Cillian',
    last_name='Murphy'
    ).first()

# Director for "A Quiet Place"


# Add artists to the database
    quiet_place_artists = [ quiet_place_artist2, quiet_place_artist3, quiet_place_artist4]
    for person in quiet_place_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "A Quiet Place"
    quiet_place_crew1 = crew.insert().values(
    artist_id=quiet_place_artist1.id,
    movie_id=35,  # A Quiet Place movie ID
    role='Actor',
    played='Evelyn Abbott'
    )

    quiet_place_crew2 = crew.insert().values(
    artist_id=quiet_place_artist2.id,
    movie_id=35,
    role='Actor',
    played='Lee Abbott'
    )

    quiet_place_crew3 = crew.insert().values(
    artist_id=quiet_place_artist3.id,
    movie_id=35,
    role='Actor',
    played='Regan Abbott'
    )

    quiet_place_crew4 = crew.insert().values(
    artist_id=quiet_place_artist4.id,
    movie_id=35,
    role='Actor',
    played='Marcus Abbott'
    )

    quiet_place_crew5 = crew.insert().values(
    artist_id=quiet_place_artist5.id,
    movie_id=35,
    role='Actor',
    played='Emmett'
    )

    quiet_place_crew6 = crew.insert().values(
    artist_id=quiet_place_artist2.id,
    movie_id=35,
    role='Director'
    )

# Add crew entries to the database
    quiet_place_crew = [quiet_place_crew1, quiet_place_crew2, quiet_place_crew3, quiet_place_crew4, quiet_place_crew5, quiet_place_crew6]
    for person in quiet_place_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "The Conjuring"
    conjuring_artist1 = Artist(
    first_name='Vera',
    last_name='Farmiga',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816623/VeraFarmiga_woabkp.jpg'
    )

    conjuring_artist2 = Artist(
    first_name='Patrick',
    last_name='Wilson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816607/PatrickWilson_fven4a.jpg'
    )

    conjuring_artist3 = Artist(
    first_name='Lili',
    last_name='Taylor',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816594/LiliTaylor_dy8wua.jpg'
    )

    conjuring_artist4 = Artist(
    first_name='Ron',
    last_name='Livingston',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816611/RonLivingston_unnvnt.jpg'
    )

    conjuring_artist5 = Artist(
    first_name='Joey',
    last_name='King',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816588/Joey_King_tumscq.webp'
    )

# Director for "The Conjuring"
    conjuring_director = Artist(
    first_name='James',
    last_name='Wan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729816584/JamesWan_jeg7o8.jpg'
    )

# Add artists to the database
    conjuring_artists = [conjuring_artist1, conjuring_artist2, conjuring_artist3, conjuring_artist4, conjuring_artist5,conjuring_director]
    for person in conjuring_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The Conjuring"
    conjuring_crew1 = crew.insert().values(
    artist_id=conjuring_artist1.id,
    movie_id=36,  # The Conjuring movie ID
    role='Actor',
    played='Lorraine Warren'
)

    conjuring_crew2 = crew.insert().values(
    artist_id=conjuring_artist2.id,
    movie_id=36,
    role='Actor',
    played='Ed Warren'
    )

    conjuring_crew3 = crew.insert().values(
    artist_id=conjuring_artist3.id,
    movie_id=36,
    role='Actor',
    played='Carolyn Perron'
    )

    conjuring_crew4 = crew.insert().values(
    artist_id=conjuring_artist4.id,
    movie_id=36,
    role='Actor',
    played='Roger Perron'
    )

    conjuring_crew5 = crew.insert().values(
    artist_id=conjuring_artist5.id,
    movie_id=36,
    role='Actor',
    played='Christine Perron'
    )

    conjuring_crew6 = crew.insert().values(
    artist_id=conjuring_director.id,
    movie_id=36,
    role='Director'
    )

# Add crew entries to the database
    conjuring_crew = [conjuring_crew1, conjuring_crew2, conjuring_crew3, conjuring_crew4, conjuring_crew5, conjuring_crew6]
    for person in conjuring_crew:
        db.session.execute(person)
    db.session.commit()



# Artists for "It Follows"
    it_follows_artist1 = Artist(
    first_name='Maika',
    last_name='Monroe',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817058/MaikaMonroe_xjhuxk.jpg'
    )

    it_follows_artist2 = Artist(
    first_name='Keir',
    last_name='Gilchrist',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817046/Keir_Gilchrist_jlu9qk.webp'
    )

    it_follows_artist3 = Artist(
    first_name='Olivia',
    last_name='Lucardi',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817074/OliviaLurccardi_f2edrq.jpg'
    )

    it_follows_artist4 = Artist(
    first_name='Jake',
    last_name='Weary',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817038/JakeWeary_xlmjjt.jpg'
    )

    it_follows_artist5 = Artist(
    first_name='Lili',
    last_name='Sepe',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817068/LiliSepe_t9admx.jpg'
    )

# Director for "It Follows"
    it_follows_director = Artist(
    first_name='David',
    last_name='Robert Mitchell',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817032/DavidMitchell_l2ypfu.jpg'
    )

# Add artists to the database
    it_follows_artists = [it_follows_artist1, it_follows_artist2, it_follows_artist3, it_follows_artist4, it_follows_artist5,it_follows_director]
    for person in it_follows_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "It Follows"
    it_follows_crew1 = crew.insert().values(
    artist_id=it_follows_artist1.id,
    movie_id=37,  # It Follows movie ID
    role='Actor',
    played='Jay Height'
    )

    it_follows_crew2 = crew.insert().values(
    artist_id=it_follows_artist2.id,
    movie_id=37,
    role='Actor',
    played='Paul'
    )

    it_follows_crew3 = crew.insert().values(
    artist_id=it_follows_artist3.id,
    movie_id=37,
    role='Actor',
    played='Yara'
    )

    it_follows_crew4 = crew.insert().values(
    artist_id=it_follows_artist4.id,
    movie_id=37,
    role='Actor',
    played='Greg'
    )

    it_follows_crew5 = crew.insert().values(
    artist_id=it_follows_artist5.id,
    movie_id=37,
    role='Actor',
    played='Kelly'
    )

    it_follows_crew6 = crew.insert().values(
    artist_id=it_follows_director.id,
    movie_id=37,
    role='Director'
    )

# Add crew entries to the database
    it_follows_crew = [it_follows_crew1, it_follows_crew2, it_follows_crew3, it_follows_crew4, it_follows_crew5, it_follows_crew6]
    for person in it_follows_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Midsommar"
    midsommar_artist1 = Artist.query.filter_by(
    first_name='Florence',
    last_name='Pugh').first()


    midsommar_artist2 = Artist(
    first_name='Jack',
    last_name='Reynor',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817839/JackReynor_rs0tnf.jpg'
    )

    midsommar_artist3 = Artist(
    first_name='William',
    last_name='Jackson Harper',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817865/william-jackson-harper-1a.jpg_ipivf6.webp'
    )

    midsommar_artist4 = Artist(
    first_name='Will',
    last_name='Poulter',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817852/Will_Poulter_qybgbj.webp'
    )

    midsommar_artist5 = Artist(
    first_name='Isabelle',
    last_name='Grill',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729817832/IsabelleGrill_afkk2x.jpg'
    )

# Director for "Midsommar"
    midsommar_director = Artist.query.filter_by(
    first_name='Ari',
    last_name='Aster',
    ).first()

# Add artists to the database
    midsommar_artists = [midsommar_artist1, midsommar_artist2, midsommar_artist3, midsommar_artist4, midsommar_artist5]
    for person in midsommar_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Midsommar"
    midsommar_crew1 = crew.insert().values(
    artist_id=midsommar_artist1.id,
    movie_id=38,  # Midsommar movie ID
    role='Actor',
    played='Dani Ardor'
    )

    midsommar_crew2 = crew.insert().values(
    artist_id=midsommar_artist2.id,
    movie_id=38,
    role='Actor',
    played='Christian Hughes'
    )

    midsommar_crew3 = crew.insert().values(
    artist_id=midsommar_artist3.id,
    movie_id=38,
    role='Actor',
    played='Josh'
    )

    midsommar_crew4 = crew.insert().values(
    artist_id=midsommar_artist4.id,
    movie_id=38,
    role='Actor',
    played='Mark'
    )

    midsommar_crew5 = crew.insert().values(
    artist_id=midsommar_artist5.id,
    movie_id=38,
    role='Actor',
    played='Maja'
    )

    midsommar_crew6 = crew.insert().values(
    artist_id=midsommar_director.id,
    movie_id=38,
    role='Director'
    )

# Add crew entries to the database
    midsommar_crew = [midsommar_crew1, midsommar_crew2, midsommar_crew3, midsommar_crew4, midsommar_crew5, midsommar_crew6]
    for person in midsommar_crew:
        db.session.execute(person)
    db.session.commit()



def undo_horror_movie_artists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.artists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM artists"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.crew RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM crew"))

    db.session.commit()
