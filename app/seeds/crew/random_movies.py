from app.models import db, Artist, environment, SCHEMA
from app.models.artist import crew
from sqlalchemy.sql import text



def seed_random_movie_artists():

    exorcist_artist1 = Artist(
        first_name='Leslie',
        last_name='Odom Jr.',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729559354/Leslie-OdomJr-Mr-Photo-Credit-Jimmy-Fontaine_h7phas.jpg'
    )

    exorcist_artist2 = Artist(
        first_name='Lidya',
        last_name='Jewett',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMmNjZDg4OTktMDNiOS00NmQ0LTkyODAtYWFiZjc3ZWExMmJhXkEyXkFqcGc_._V1__paw6mp.jpg'
    )

    exorcist_artist3 = Artist(
        first_name='Olivia',
        last_name='Marcum',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562595/olivia.jpg_kuxijy.webp'
    )

    exorcist_artist4 = Artist(
        first_name='Jennifer',
        last_name='Nettles',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMTgzMzc5ODUxMl5BMl5BanBnXkFtZTcwOTkzMDYxMw_._V1__dof6zm.jpg'
    )

    exorcist_artist5 = Artist(
        first_name='Norbert',
        last_name='Leo Butz',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562595/web_cast_norbertleobutz_fosse-verdon_570x698.jpg_xc7sia.avif'
    )

    exorcist_artist6 = Artist(
        first_name='Ann',
        last_name='Dowd',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMjIwMTc0NzA0OV5BMl5BanBnXkFtZTcwMDIwMjk4OA_._V1__n9znba.jpg'
    )

    exorcist_artist7 = Artist(
        first_name='Ellen',
        last_name='Burstyn',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMTU4MjYxMDc3MF5BMl5BanBnXkFtZTYwNzU3MDIz._V1__msdcrc.jpg'
    )

    exorcist_artist8 = Artist(
        first_name='Raphael',
        last_name='Sbarge',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562595/MV5BOTEwM2E1ZGQtYTJhMi00MmUwLTgyNGYtZGVkZDc2NWU4NDZmXkEyXkFqcGc_._V1__umcope.jpg'
    )
    exorcist_artist9 = Artist(
        first_name='David',
        last_name='Gordon Green',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562593/MV5BMTYyNjI3NTUwOF5BMl5BanBnXkFtZTYwMTg1NjY1._V1__mdhom6.jpg'
    )

    exorcist_artist10 = Artist(
        first_name='Jason',
        last_name='Blum',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMTgyMDU1OTQ5Ml5BMl5BanBnXkFtZTcwNTEzMDY1OA_._V1__lh22rn.jpg'
    )

    exorcist_artist11 = Artist(
        first_name='David',
        last_name='Robinson',
        img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729562592/MV5BMTg3NzU1NzcwNF5BMl5BanBnXkFtZTcwNTc2NDMxNw_._V1__xjqqkk.jpg'
    )


    exorcist = [exorcist_artist1,exorcist_artist2,exorcist_artist3,exorcist_artist4,exorcist_artist5,exorcist_artist6,exorcist_artist7,exorcist_artist8,exorcist_artist9,exorcist_artist10,exorcist_artist11]
    for person in exorcist:
        db.session.add(person)

    db.session.commit()

    exorcist_crew1 = crew.insert().values(
        artist_id=exorcist_artist1.id,
        movie_id=1,
        role='Actor',
        played='Victor Fielding'
    )

    exorcist_crew2 = crew.insert().values(
        artist_id=exorcist_artist2.id,
        movie_id=1,
        role='Actor',
        played='Angela Fielding'
    )

    exorcist_crew3 = crew.insert().values(
        artist_id=exorcist_artist3.id,
        movie_id=1,
        role='Actor',
        played='Katherine West'
    )

    exorcist_crew4 = crew.insert().values(
        artist_id=exorcist_artist4.id,
        movie_id=1,
        role='Actor',
        played='Miranda West'
    )

    exorcist_crew5 = crew.insert().values(
        artist_id=exorcist_artist5.id,
        movie_id=1,
        role='Actor',
        played='Tony West'
    )

    exorcist_crew6 = crew.insert().values(
        artist_id=exorcist_artist6.id,
        movie_id=1,
        role='Actor',
        played='Ann'
    )

    exorcist_crew7 = crew.insert().values(
        artist_id=exorcist_artist7.id,
        movie_id=1,
        role='Actor',
        played='Chris MacNeil'
    )

    exorcist_crew8 = crew.insert().values(
        artist_id=exorcist_artist8.id,
        movie_id=1,
        role='Actor',
        played='Pastor Don Revans​'
    )

    exorcist_crew9 = crew.insert().values(
        artist_id=exorcist_artist9.id,
        movie_id=1,
        role='Director',
    )
    exorcist_crew10 = crew.insert().values(
        artist_id=exorcist_artist10.id,
        movie_id=1,
        role='Producer',
    )
    exorcist_crew11 = crew.insert().values(
        artist_id=exorcist_artist11.id,
        movie_id=1,
        role='Producer',
    )

    exorcist_crew = [exorcist_crew1,exorcist_crew2,exorcist_crew3,exorcist_crew4,exorcist_crew5,exorcist_crew6,exorcist_crew7,exorcist_crew8,exorcist_crew9,exorcist_crew10,exorcist_crew11]

    for person in exorcist_crew:
        db.session.execute(person)
    db.session.commit()



    # Artists for "Killers of the Flower Moon"
    killer_artist1 = Artist(
    first_name='Leonardo',
    last_name='DiCaprio',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563148/MV5BMjI0MTg3MzI0M15BMl5BanBnXkFtZTcwMzQyODU2Mw_._V1_FMjpg_UX1000__dbjqax.jpg'
    )

    killer_artist2 = Artist(
    first_name='Robert',
    last_name='De Niro',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563184/MV5BMjAwNDU3MzcyOV5BMl5BanBnXkFtZTcwMjc0MTIxMw_._V1_FMjpg_UX1000__agyb4p.jpg'
    )

    killer_artist3 = Artist(
    first_name='Lily',
    last_name='Gladstone',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563233/7ca7342649cd8aac848ed8c6b6e0a6c82b-2023-0629-Lily-Gladstone27464-5.rvertical.w570.jpg_w05q8w.webp'
        )

    killer_artist4 = Artist(
    first_name='Tantoo',
    last_name='Cardinal',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563549/Judge_Tantoo_Cardinal_vmgx2n.jpg'
    )

    killer_artist5 = Artist(
    first_name='Jesse',
    last_name='Plemons',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563548/Jesse_Plemons__20769593584___cropped_vi38t6.jpg'
    )

    killer_artist6 = Artist(
    first_name='Cara',
    last_name='Jade Myers',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729563559/MV5BMDg2ODBjOGQtNGRjYS00NDk4LTllMzItM2U0MzY4MjA0NTlhXkEyXkFqcGc_._V1__tqksk0.jpg'
    )

    killer_artist9 = Artist(
    first_name='Martin',
    last_name='Scorsese',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729564155/Martin_Scorsese_MFF_2023_kihxna.jpg'
    )

    killer_artist10 = Artist(
    first_name='Dan',
    last_name='Friedkin',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729564167/MV5BYzE5NDY1ZjEtNjQ4OC00Yzc5LTljNjEtZTM2NWNmYmViNjNiXkEyXkFqcGc_._V1_QL75_UX140_CR0_1_140_207__ak7sa6.jpg'
    )

    killer_artist11 = Artist(
    first_name='Brad',
    last_name='Fisher',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729564204/MV5BMjI4MzY3NzU0MF5BMl5BanBnXkFtZTgwNjM2ODk3MzE_._V1_FMjpg_UX1000__ocmz8b.jpg'

    )

# Add artists to the database
    killers = [killer_artist1, killer_artist2, killer_artist3, killer_artist4, killer_artist5, killer_artist6,killer_artist9,killer_artist10,killer_artist11]
    for person in killers:
        db.session.add(person)

    db.session.commit()


    killers_crew1 = crew.insert().values(
    artist_id=killer_artist1.id,
    movie_id=2,
    role='Actor',
    played='Ernest Burkhart'
    )

    killers_crew2 = crew.insert().values(
    artist_id=killer_artist2.id,
    movie_id=2,
    role='Actor',
    played='William Hale'
    )

    killers_crew3 = crew.insert().values(
    artist_id=killer_artist3.id,
    movie_id=2,
    role='Actor',
    played='Mollie Burkhart'
)

    killers_crew4 = crew.insert().values(
    artist_id=killer_artist4.id,
    movie_id=2,
    role='Actor',
    played='Anna Brown'
)

    killers_crew5 = crew.insert().values(
    artist_id=killer_artist5.id,
    movie_id=2,
    role='Actor',
    played='Tom White'
    )

    killers_crew6 = crew.insert().values(
    artist_id=killer_artist6.id,
    movie_id=2,
    role='Actor',
    played='Bryan Burkhart'
)

    killers_crew9 = crew.insert().values(
    artist_id=killer_artist9.id,
    movie_id=2,
    role='Director',
    )

    killers_crew10 = crew.insert().values(
    artist_id=killer_artist10.id,
    movie_id=2,
    role='Producer',
    )

    killers_crew11 = crew.insert().values(
    artist_id=killer_artist11.id,
    movie_id=2,
    role='Producer',
    )

# Add crew entries to the database
    killers_crew = [killers_crew1, killers_crew2, killers_crew3, killers_crew4, killers_crew5, killers_crew6, killers_crew9, killers_crew10, killers_crew11]
    for person in killers_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "The Creator"
    creator_artist1 = Artist(
    first_name='John',
    last_name='David Washington',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631006/JohnDavidWashington_diaujz.jpg'
    )

    creator_artist3 = Artist(
    first_name='Ken',
    last_name='Watanabe',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631088/KenWantable_v5p7of.jpg'
    )

    creator_artist4 = Artist(
    first_name='Gemma',
    last_name='Chan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729630998/GemmaChan_y3nrun.jpg'
    )

    creator_artist5 = Artist(
    first_name='Madeline',
    last_name='Yuna Voiles',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631118/MadeleineYuna_rvur2u.jpg'
    )

    creator_artist7 = Artist(
    first_name='Gareth',
    last_name='Edwards',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729630987/garethEdwards_y5snmf.jpg'
    )


# Add artists to the database
    creators = [creator_artist1, creator_artist3, creator_artist4, creator_artist5, creator_artist7]
    for person in creators:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The Creator"
    creator_crew1 = crew.insert().values(
    artist_id=creator_artist1.id,
    movie_id=3,
    role='Actor',
    played='Joshua'
    )


    creator_crew3 = crew.insert().values(
    artist_id=creator_artist3.id,
    movie_id=3,
    role='Actor',
    played='Harun'
    )

    creator_crew4 = crew.insert().values(
    artist_id=creator_artist4.id,
    movie_id=3,
    role='Actor',
    played='Maya'
    )

    creator_crew5 = crew.insert().values(
    artist_id=creator_artist5.id,
    movie_id=3,
    role='Actor',
    played='Alphie'
    )

    creator_crew7 = crew.insert().values(
    artist_id=creator_artist7.id,
    movie_id=3,
    role='Director'
    )


# Add crew entries to the database
    creator_crew = [creator_crew1, creator_crew3, creator_crew4, creator_crew5, creator_crew7]
    for person in creator_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "A Haunting in Venice"
    haunting_artist1 = Artist(
    first_name='Kenneth',
    last_name='Branagh',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631804/Kenneth_d3evih.jpg'
    )

    haunting_artist2 = Artist(
    first_name='Michelle',
    last_name='Yeoh',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631824/Michelle_qpu8yb.webp'
    )

    haunting_artist3 = Artist(
    first_name='Jamie',
    last_name='Dornan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631795/Jamie_bvuuyl.jpg'
    )

    haunting_artist4 = Artist(
    first_name='Camille',
    last_name='Cottin',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631781/Camille_fcyt9s.webp'
    )

    haunting_artist5 = Artist(
    first_name='Kelly',
    last_name='Reilly',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729631788/Kelly_lzoby9.jpg'
    )


# Add artists to the database
    haunting_artists = [haunting_artist1, haunting_artist2, haunting_artist3, haunting_artist4, haunting_artist5]
    for person in haunting_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "A Haunting in Venice"
    haunting_crew1 = crew.insert().values(
    artist_id=haunting_artist1.id,
    movie_id=4,  # Replace with actual movie ID
    role='Actor',
    played='Hercule Poirot'
    )

    haunting_crew2 = crew.insert().values(
    artist_id=haunting_artist2.id,
    movie_id=4,
    role='Actor',
    played='Joyce Reynolds'
    )

    haunting_crew3 = crew.insert().values(
    artist_id=haunting_artist3.id,
    movie_id=4,
    role='Actor',
    played='Dr Lesile Ferrier'
    )

    haunting_crew4 = crew.insert().values(
    artist_id=haunting_artist4.id,
    movie_id=4,
    role='Actor',
    played='Olga Seminoff'
    )

    haunting_crew5 = crew.insert().values(
    artist_id=haunting_artist5.id,
    movie_id=4,
    role='Actor',
    played='Rowenna Drake'
    )

    haunting_crew6 = crew.insert().values(
    artist_id=haunting_artist1.id,
    movie_id=4,
    role='Director'
    )

# Add crew entries to the database
    haunting_crew = [haunting_crew1, haunting_crew2, haunting_crew3, haunting_crew4, haunting_crew5, haunting_crew6]
    for person in haunting_crew:
        db.session.execute(person)
    db.session.commit()

        # Artists for "Dumb Money"
    dumbmoney_artist1 = Artist(
    first_name='Paul',
    last_name='Dano',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633135/PaulDano_foempx.jpg'
    )

    dumbmoney_artist2 = Artist(
    first_name='Seth',
    last_name='Rogen',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633137/Seth_mv3wnn.jpg'
    )

    dumbmoney_artist3 = Artist(
    first_name='Vincent',
    last_name="D'Onofrio",
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633127/Vincent_vqj1pr.jpg'
    )

    dumbmoney_artist4 = Artist(
    first_name='America',
    last_name='Ferrera',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633096/America_xkcxkp.jpg'
    )

    dumbmoney_artist5 = Artist(
    first_name='=Talia',
    last_name='Ryder',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633140/Talia_a3prps.jpg'
    )

# Director for "Dumb Money"
    dumbmoney_director = Artist(
    first_name='Craig',
    last_name='Gillespie',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633188/craig_onqtk5.webp'
    )

# Add artists to the database
    dumbmoney_artists = [dumbmoney_artist1, dumbmoney_artist2, dumbmoney_artist3, dumbmoney_artist4, dumbmoney_artist5,dumbmoney_director]
    for person in dumbmoney_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Dumb Money"
    dumbmoney_crew1 = crew.insert().values(
    artist_id=dumbmoney_artist1.id,
    movie_id=5,  # Replace with actual movie ID
    role='Actor',
    played='Keith Gill'
    )

    dumbmoney_crew2 = crew.insert().values(
    artist_id=dumbmoney_artist2.id,
    movie_id=5,
    role='Actor',
    played='Gabe Plotkin'
    )

    dumbmoney_crew3 = crew.insert().values(
    artist_id=dumbmoney_artist3.id,
    movie_id=5,
    role='Actor',
    played='Steve Cohen'
    )

    dumbmoney_crew4 = crew.insert().values(
    artist_id=dumbmoney_artist4.id,
    movie_id=5,
    role='Actor',
    played='Jenny'
    )

    dumbmoney_crew5 = crew.insert().values(
    artist_id=dumbmoney_artist5.id,
    movie_id=5,
    role='Actor',
    played='Harmony Williams'
    )

    dumbmoney_crew6 = crew.insert().values(
    artist_id=dumbmoney_director.id,
    movie_id=5,
    role='Director'
    )

# Add crew entries to the database
    dumbmoney_crew = [dumbmoney_crew1, dumbmoney_crew2, dumbmoney_crew3, dumbmoney_crew4, dumbmoney_crew5, dumbmoney_crew6]
    for person in dumbmoney_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Blue Beetle"
    bluebeetle_artist1 = Artist(
    first_name='Xolo',
    last_name='Maridueña',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633911/Xolo_vxnt9x.jpg'
    )

    bluebeetle_artist2 = Artist(
    first_name='Bruna',
    last_name='Marquezine',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633898/Bruna_megqin.jpg'
    )

    bluebeetle_artist3 = Artist(
    first_name='Raoul',
    last_name='Max Trujillo',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633984/Raoul_sbucvz.webp'
    )

    bluebeetle_artist4 = Artist(
    first_name='George',
    last_name='Lopez',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633902/george_ppmm0b.jpg'
    )

    bluebeetle_artist5 = Artist(
    first_name='Adriana',
    last_name='Barraza',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633889/adriana_a4jd6x.jpg'
    )

    # Director for "Blue Beetle"
    bluebeetle_director = Artist(
    first_name='Angel',
    last_name='Manuel Soto',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729633895/angel_eeppkc.jpg'
    )

# Add artists to the database
    bluebeetle_artists = [bluebeetle_artist1, bluebeetle_artist2, bluebeetle_artist3, bluebeetle_artist4, bluebeetle_artist5,bluebeetle_director]
    for person in bluebeetle_artists:
        db.session.add(person)

    db.session.commit()

    # Crew entries for "Blue Beetle"
    bluebeetle_crew1 = crew.insert().values(
    artist_id=bluebeetle_artist1.id,
    movie_id=6,  # Replace with actual movie ID
    role='Actor',
    played='Jaime Reyes / Blue Beetle'
    )

    bluebeetle_crew2 = crew.insert().values(
    artist_id=bluebeetle_artist2.id,
    movie_id=6,
    role='Actor',
    played='Pilar Reyes'
    )

    bluebeetle_crew3 = crew.insert().values(
    artist_id=bluebeetle_artist3.id,
    movie_id=6,
    role='Actor',
    played='Carapax'
    )

    bluebeetle_crew4 = crew.insert().values(
    artist_id=bluebeetle_artist4.id,
    movie_id=6,
    role='Actor',
    played='Uncle Rudy'
    )

    bluebeetle_crew5 = crew.insert().values(
    artist_id=bluebeetle_artist5.id,
    movie_id=6,
    role='Actor',
    played='Nana Reyes'
    )

    bluebeetle_crew6 = crew.insert().values(
    artist_id=bluebeetle_director.id,
    movie_id=6,
    role='Director'
    )

# Add crew entries to the database
    bluebeetle_crew = [bluebeetle_crew1, bluebeetle_crew2, bluebeetle_crew3, bluebeetle_crew4, bluebeetle_crew5, bluebeetle_crew6]
    for person in bluebeetle_crew:
        db.session.execute(person)
    db.session.commit()



    # Artists for "Gran Turismo"
    gran_turismo_artist1 = Artist(
    first_name='David',
    last_name='Harbour',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729634419/David_Harbour_otjthv.webp'
    )

    gran_turismo_artist2 = Artist(
    first_name='Orlando',
    last_name='Bloom',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729634442/Orlando_meuzd4.jpg'
    )

    gran_turismo_artist3 = Artist(
    first_name='Archie',
    last_name='Madekwe',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729634407/Archie_opntdh.jpg'
    )

    gran_turismo_artist4 = Artist(
    first_name='Darren',
    last_name='Barnet',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729634416/Darren_fb9p64.jpg'
    )

# Director for "Gran Turismo"
    gran_turismo_director = Artist(
    first_name='Neal',
    last_name='Hargrove',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729634434/Neil_yiqz9n.jpg'
    )

# Add artists to the database
    gran_turismo_artists = [gran_turismo_artist1, gran_turismo_artist2, gran_turismo_artist3, gran_turismo_artist4,gran_turismo_director]
    for person in gran_turismo_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Gran Turismo"
    gran_turismo_crew1 = crew.insert().values(
    artist_id=gran_turismo_artist1.id,
    movie_id=7,  # Replace with actual movie ID
    role='Actor',
    played='Jack Salter'
    )

    gran_turismo_crew2 = crew.insert().values(
    artist_id=gran_turismo_artist2.id,
    movie_id=7,
    role='Actor',
    played='Danny Moore'
    )

    gran_turismo_crew3 = crew.insert().values(
    artist_id=gran_turismo_artist3.id,
    movie_id=7,
    role='Actor',
    played='Jann Mardenborough'
    )

    gran_turismo_crew4 = crew.insert().values(
    artist_id=gran_turismo_artist4.id,
    movie_id=7,
    role='Actor',
    played='Matty Davis'
    )


    gran_turismo_crew6 = crew.insert().values(
    artist_id=gran_turismo_director.id,
    movie_id=7,
    role='Director'
    )

# Add crew entries to the database
    gran_turismo_crew = [gran_turismo_crew1, gran_turismo_crew2, gran_turismo_crew3, gran_turismo_crew4, gran_turismo_crew6]
    for person in gran_turismo_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Haunted Mansion" (2024)
    haunted_mansion_artist1 = Artist(
    first_name='LaKeith',
    last_name='Stanfield',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729645971/Lakeiith_a5s6m2.jpg'
    )

    haunted_mansion_artist2 = Artist(
    first_name='Tiffany',
    last_name='Haddish',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729645984/tiffany-haddish_qpcgdo.jpg'
    )

    haunted_mansion_artist3 = Artist(
    first_name='Owen',
    last_name='Wilson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646024/OwenWIlson_stugu4.jpg'
    )

    haunted_mansion_artist4 = Artist(
    first_name='Danny',
    last_name='DeVito',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729645941/DannyD_mokqbq.jpg'
    )

    haunted_mansion_artist5 = Artist(
    first_name='Rosario',
    last_name='Dawson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729645992/RosarioDawson_deg7p4.jpg'
    )

# Director for "Haunted Mansion" (2024)
    haunted_mansion_director = Artist(
    first_name='Justin',
    last_name='Simien',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729645956/JustinSimien_zxqnrm.jpg'
    )

# Add artists to the database
    haunted_mansion_artists = [haunted_mansion_artist1, haunted_mansion_artist2, haunted_mansion_artist3, haunted_mansion_artist4, haunted_mansion_artist5,haunted_mansion_director]
    for person in haunted_mansion_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Haunted Mansion" (2024)
    haunted_mansion_crew1 = crew.insert().values(
    artist_id=haunted_mansion_artist1.id,
    movie_id=8,  # Replace with actual movie ID
    role='Actor',
    played='Ben Matthias'
    )

    haunted_mansion_crew2 = crew.insert().values(
    artist_id=haunted_mansion_artist2.id,
    movie_id=8,
    role='Actor',
    played='Harriet'
    )

    haunted_mansion_crew3 = crew.insert().values(
    artist_id=haunted_mansion_artist3.id,
    movie_id=8,
    role='Actor',
    played='Kent'
    )

    haunted_mansion_crew4 = crew.insert().values(
    artist_id=haunted_mansion_artist4.id,
    movie_id=8,
    role='Actor',
    played='Bruce Davis'
    )

    haunted_mansion_crew5 = crew.insert().values(
    artist_id=haunted_mansion_artist5.id,
    movie_id=8,
    role='Actor',
    played='Gabbie'
    )

    haunted_mansion_crew6 = crew.insert().values(
    artist_id=haunted_mansion_director.id,
    movie_id=8,
    role='Director'
    )

# Add crew entries to the database
    haunted_mansion_crew = [haunted_mansion_crew1, haunted_mansion_crew2, haunted_mansion_crew3, haunted_mansion_crew4, haunted_mansion_crew5, haunted_mansion_crew6]
    for person in haunted_mansion_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Barbie" (2023)
    barbie_artist1 = Artist(
    first_name='Margot',
    last_name='Robbie',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646674/MargotRobbie_xcbbvp.webp'
    )

    barbie_artist2 = Artist(
    first_name='Ryan',
    last_name='Gosling',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646629/RyanGosling_bz1ifc.webp'
    )
    barbie_artist4 = Artist(
    first_name='Kate',
    last_name='McKinnon',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646618/KateMcKinnon_htudkf.jpg'
    )

    barbie_artist5 = Artist(
    first_name='Issa',
    last_name='Rae',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646609/IssaRae_pj1a9p.jpg'
    )

# Director for "Barbie" (2023)
    barbie_director = Artist(
    first_name='Greta',
    last_name='Gerwig',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729646696/GretaGerwig_g9ppe0.webp'
    )

# Add artists to the database
    barbie_artists = [barbie_artist1, barbie_artist2, barbie_artist4, barbie_artist5,barbie_director]
    for person in barbie_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Barbie" (2023)
    barbie_crew1 = crew.insert().values(
    artist_id=barbie_artist1.id,
    movie_id=9,  # Replace with actual movie ID
    role='Actor',
    played='Barbie'
    )

    barbie_crew2 = crew.insert().values(
    artist_id=barbie_artist2.id,
    movie_id=9,
    role='Actor',
    played='Ken'
    )

    barbie_artist3 = Artist.query.filter_by(first_name='America',last_name='Ferrera').first()
    barbie_crew3 = crew.insert().values(
    artist_id=barbie_artist3.id,
    movie_id=9,
    role='Actor',
    played='Gloria'
    )

    barbie_crew4 = crew.insert().values(
    artist_id=barbie_artist4.id,
    movie_id=9,
    role='Actor',
    played='Weird Barbie'
    )

    barbie_crew5 = crew.insert().values(
    artist_id=barbie_artist5.id,
    movie_id=9,
    role='Actor',
    played='President Barbie'
    )

    barbie_crew6 = crew.insert().values(
    artist_id=barbie_director.id,
    movie_id=9,
    role='Director'
    )

# Add crew entries to the database
    barbie_crew = [barbie_crew1, barbie_crew2, barbie_crew3, barbie_crew4, barbie_crew5, barbie_crew6]
    for person in barbie_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Oppenheimer"
    oppenheimer_artist1 = Artist(
    first_name='Cillian',
    last_name='Murphy',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647081/CillianMurphy_dqqmxk.webp'
    )

    oppenheimer_artist2 = Artist(
    first_name='Emily',
    last_name='Blunt',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647092/EmilyBlunt_mucor4.webp'
    )

    oppenheimer_artist3 = Artist(
    first_name='Matt',
    last_name='Damon',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647055/MattDamon_wj22ec.jpg'
    )

    oppenheimer_artist4 = Artist(
    first_name='Robert',
    last_name='Downey Jr.',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647066/RDJ_crmnwv.webp'
    )

    oppenheimer_artist5 = Artist(
    first_name='Florence',
    last_name='Pugh',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647099/FlorencePugh_mgggmq.webp'
    )

# Director for "Oppenheimer"
    oppenheimer_director = Artist(
    first_name='Christopher',
    last_name='Nolan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647163/ChristoperNolan_x3asd3.jpg'
    )

# Add artists to the database
    oppenheimer_artists = [oppenheimer_artist1, oppenheimer_artist2, oppenheimer_artist3, oppenheimer_artist4, oppenheimer_artist5,oppenheimer_director]
    for person in oppenheimer_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Oppenheimer"
    oppenheimer_crew1 = crew.insert().values(
    artist_id=oppenheimer_artist1.id,
    movie_id=10,  # Replace with actual movie ID
    role='Actor',
    played='J. Robert Oppenheimer'
    )

    oppenheimer_crew2 = crew.insert().values(
    artist_id=oppenheimer_artist2.id,
    movie_id=10,
    role='Actor',
    played='Kitty Oppenheimer'
    )

    oppenheimer_crew3 = crew.insert().values(
    artist_id=oppenheimer_artist3.id,
    movie_id=10,
    role='Actor',
    played='Gen. Leslie Groves'
    )

    oppenheimer_crew4 = crew.insert().values(
    artist_id=oppenheimer_artist4.id,
    movie_id=10,
    role='Actor',
    played='Lewis Strauss'
    )

    oppenheimer_crew5 = crew.insert().values(
    artist_id=oppenheimer_artist5.id,
    movie_id=10,
    role='Actor',
    played='Jean Tatlock'
    )

    oppenheimer_crew6 = crew.insert().values(
    artist_id=oppenheimer_director.id,
    movie_id=10,
    role='Director'
    )

# Add crew entries to the database
    oppenheimer_crew = [oppenheimer_crew1, oppenheimer_crew2, oppenheimer_crew3, oppenheimer_crew4, oppenheimer_crew5, oppenheimer_crew6]
    for person in oppenheimer_crew:
        db.session.execute(person)
    db.session.commit()


def undo_random_movie_artists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.artists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM artists"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.crew RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM crew"))

    db.session.commit()
