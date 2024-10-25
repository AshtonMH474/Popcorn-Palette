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

    # Artists for "Bridesmaids"
    bridesmaids_artist1 = Artist(
    first_name='Kristen',
    last_name='Wiig',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809340/KristinWiig_t0emxg.jpg'
    )

    bridesmaids_artist2 = Artist(
    first_name='Maya',
    last_name='Rudolph',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809341/MayaRudolph_mjudmo.jpg'
    )

    bridesmaids_artist3 = Artist(
    first_name='Rose',
    last_name='Byrne',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809378/RoseByrne_pgsnjf.jpg'
    )

    bridesmaids_artist4 = Artist(
    first_name='Melissa',
    last_name='McCarthy',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809459/Melissa-McCarthy-Comic_kwsmze.webp'
    )

    bridesmaids_artist5 = Artist(
    first_name='Wendi',
    last_name='McLendon-Covey',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809387/WendiMclendon_enjtw8.jpg'
    )

# Director for "Bridesmaids"
    bridesmaids_director = Artist(
    first_name='Paul',
    last_name='Feig',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809396/Paul_Feig_swlits.webp'
    )

# Add artists to the database
    bridesmaids_artists = [bridesmaids_artist1, bridesmaids_artist2, bridesmaids_artist3, bridesmaids_artist4, bridesmaids_artist5,bridesmaids_director]
    for person in bridesmaids_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Bridesmaids"
    bridesmaids_crew1 = crew.insert().values(
    artist_id=bridesmaids_artist1.id,
    movie_id=25,  # Bridesmaids movie ID
    role='Actor',
    played='Annie Walker'
    )

    bridesmaids_crew2 = crew.insert().values(
    artist_id=bridesmaids_artist2.id,
    movie_id=25,
    role='Actor',
    played='Lillian Donovan'
    )

    bridesmaids_crew3 = crew.insert().values(
    artist_id=bridesmaids_artist3.id,
    movie_id=25,
    role='Actor',
    played='Helen'
    )

    bridesmaids_crew4 = crew.insert().values(
    artist_id=bridesmaids_artist4.id,
    movie_id=25,
    role='Actor',
    played='Megan Price'
    )

    bridesmaids_crew5 = crew.insert().values(
    artist_id=bridesmaids_artist5.id,
    movie_id=25,
    role='Actor',
    played='Becca'
    )

    bridesmaids_crew6 = crew.insert().values(
    artist_id=bridesmaids_director.id,
    movie_id=25,
    role='Director'
    )

# Add crew entries to the database
    bridesmaids_crew = [bridesmaids_crew1, bridesmaids_crew2, bridesmaids_crew3, bridesmaids_crew4, bridesmaids_crew5, bridesmaids_crew6]
    for person in bridesmaids_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Step Brothers"
    step_brothers_artist1 = Artist(
    first_name='Will',
    last_name='Ferrell',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809948/Will-Ferrell_f1uavp.webp'
    )

    step_brothers_artist2 = Artist(
    first_name='John',
    last_name='C. Reilly',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809911/JohnCReilly_vbnnmi.webp'
    )

    step_brothers_artist3 = Artist(
    first_name='Mary',
    last_name='Steenburgen',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809938/Mary-Steenburgen-2018_khf9pm.webp'
    )

    step_brothers_artist4 = Artist(
    first_name='Richard',
    last_name='Jenkins',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809961/RichardJenkins_uqavy3.jpg'
    )

    step_brothers_artist5 = Artist(
    first_name='Kathryn',
    last_name='Hahn',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809925/Kathryn_Hahn_ntyazb.webp'
    )

# Director for "Step Brothers"
    step_brothers_director = Artist(
    first_name='Adam',
    last_name='McKay',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729809899/AdamMckay_fippzj.jpg'
    )

# Add artists to the database
    step_brothers_artists = [step_brothers_artist1, step_brothers_artist2, step_brothers_artist3, step_brothers_artist4, step_brothers_artist5,step_brothers_director]
    for person in step_brothers_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Step Brothers"
    step_brothers_crew1 = crew.insert().values(
    artist_id=step_brothers_artist1.id,
    movie_id=26,  # Step Brothers movie ID
    role='Actor',
    played='Brennan Huff'
    )

    step_brothers_crew2 = crew.insert().values(
    artist_id=step_brothers_artist2.id,
    movie_id=26,
    role='Actor',
    played='Dale Doback'
    )

    step_brothers_crew3 = crew.insert().values(
    artist_id=step_brothers_artist3.id,
    movie_id=26,
    role='Actor',
    played='Nancy Huff'
        )

    step_brothers_crew4 = crew.insert().values(
    artist_id=step_brothers_artist4.id,
    movie_id=26,
    role='Actor',
    played='Robert Doback'
    )

    step_brothers_crew5 = crew.insert().values(
    artist_id=step_brothers_artist5.id,
    movie_id=26,
    role='Actor',
    played='Alice'
    )

    step_brothers_crew6 = crew.insert().values(
    artist_id=step_brothers_director.id,
    movie_id=26,
    role='Director'
    )

# Add crew entries to the database
    step_brothers_crew = [step_brothers_crew1, step_brothers_crew2, step_brothers_crew3, step_brothers_crew4, step_brothers_crew5, step_brothers_crew6]
    for person in step_brothers_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "Groundhog Day"
    groundhog_day_artist1 = Artist(
    first_name='Bill',
    last_name='Murray',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810345/BillMurray_endlbr.jpg'
    )

    groundhog_day_artist2 = Artist(
    first_name='Andie',
    last_name='MacDowell',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810340/andie-mcdowell0324_kpst6v.avif'
    )

    groundhog_day_artist3 = Artist(
    first_name='Chris',
    last_name='Elliott',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810355/ChirsElliot_g1j0ln.jpg'
    )

    groundhog_day_artist4 = Artist(
    first_name='Stephen',
    last_name='Tobolowsky',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810370/Stephen_Tobolowsky_ucxhba.webp'
    )

    groundhog_day_artist5 = Artist(
    first_name='Brian',
    last_name='Doyle-Murray',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810353/BrianDoyleMurray_ypbxed.jpg'
    )

# Director for "Groundhog Day"
    groundhog_day_director = Artist(
    first_name='Harold',
    last_name='Ramis',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810361/Harold_Ramis_Oct_2009_f6lz6q.jpg'
    )

# Add artists to the database
    groundhog_day_artists = [groundhog_day_artist1, groundhog_day_artist2, groundhog_day_artist3, groundhog_day_artist4, groundhog_day_artist5,groundhog_day_director ]
    for person in groundhog_day_artists:
        db.session.add(person)

    db.session.commit()




# Crew entries for "Groundhog Day"
    groundhog_day_crew1 = crew.insert().values(
    artist_id=groundhog_day_artist1.id,
    movie_id=27,  # Groundhog Day movie ID
    role='Actor',
    played='Phil Connors'
    )

    groundhog_day_crew2 = crew.insert().values(
    artist_id=groundhog_day_artist2.id,
    movie_id=27,
    role='Actor',
    played='Rita'
    )

    groundhog_day_crew3 = crew.insert().values(
    artist_id=groundhog_day_artist3.id,
    movie_id=27,
    role='Actor',
    played='Larry'
    )

    groundhog_day_crew4 = crew.insert().values(
    artist_id=groundhog_day_artist4.id,
    movie_id=27,
    role='Actor',
    played='Ned Ryerson'
    )

    groundhog_day_crew5 = crew.insert().values(
    artist_id=groundhog_day_artist5.id,
    movie_id=27,
    role='Actor',
    played='Buster Green'
    )

    groundhog_day_crew6 = crew.insert().values(
    artist_id=groundhog_day_director.id,
    movie_id=27,
    role='Director'
    )

# Add crew entries to the database
    groundhog_day_crew = [groundhog_day_crew1, groundhog_day_crew2, groundhog_day_crew3, groundhog_day_crew4, groundhog_day_crew5, groundhog_day_crew6]
    for person in groundhog_day_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "Mean Girls"
    mean_girls_artist1 = Artist(
    first_name='Lindsay',
    last_name='Lohan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810936/LindsayLohan_i6exyy.jpg'
    )

    mean_girls_artist2 = Artist(
    first_name='Rachel',
    last_name='McAdams',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810980/Rachel_McAdams_2016_bgti2n.jpg'
    )

    mean_girls_artist3 = Artist(
    first_name='Tina',
    last_name='Fey',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810952/TinaFey_svqeb3.jpg'
    )

    mean_girls_artist4 = Artist(
    first_name='Amanda',
    last_name='Seyfried',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810910/AmanadaSeyfried_sodsxm.jpg'
    )

    mean_girls_artist5 = Artist(
    first_name='Lizzy',
    last_name='Caplan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810938/Lizzie_Caplan_CC2012_xapyzu.jpg'
    )

# Director for "Mean Girls"
    mean_girls_director = Artist(
    first_name='Mark',
    last_name='Waters',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729810943/Mark_Waters_mxa1gx.webp'
    )

# Add artists to the database
    mean_girls_artists = [mean_girls_artist1, mean_girls_artist2, mean_girls_artist3, mean_girls_artist4, mean_girls_artist5,mean_girls_director]
    for person in mean_girls_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Mean Girls"
    mean_girls_crew1 = crew.insert().values(
    artist_id=mean_girls_artist1.id,
    movie_id=28,  # Mean Girls movie ID
    role='Actor',
    played='Cady Heron'
    )

    mean_girls_crew2 = crew.insert().values(
    artist_id=mean_girls_artist2.id,
    movie_id=28,
    role='Actor',
    played='Regina George'
    )

    mean_girls_crew3 = crew.insert().values(
    artist_id=mean_girls_artist3.id,
    movie_id=28,
    role='Actor',
    played='Ms. Norbury'
    )

    mean_girls_crew4 = crew.insert().values(
    artist_id=mean_girls_artist4.id,
    movie_id=28,
    role='Actor',
    played='Karen Smith'
    )

    mean_girls_crew5 = crew.insert().values(
    artist_id=mean_girls_artist5.id,
    movie_id=28,
    role='Actor',
    played='Janice Ian'
    )

    mean_girls_crew6 = crew.insert().values(
    artist_id=mean_girls_director.id,
    movie_id=28,
    role='Director'
    )

# Add crew entries to the database
    mean_girls_crew = [mean_girls_crew1, mean_girls_crew2, mean_girls_crew3, mean_girls_crew4, mean_girls_crew5, mean_girls_crew6]
    for person in mean_girls_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "Dumb and Dumber"
    dumb_and_dumber_artist1 = Artist(
    first_name='Jim',
    last_name='Carrey',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729811981/Jim-Carrey-2012.jpg_q0cxyl.webp'
    )

    dumb_and_dumber_artist2 = Artist(
    first_name='Jeff',
    last_name='Daniels',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729811978/JeffDaniels_mjq0qs.jpg'
    )

    dumb_and_dumber_artist3 = Artist(
    first_name='Lauren',
    last_name='Holly',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729811995/LaurenHolly_c5zren.jpg'
    )

    dumb_and_dumber_artist4 = Artist(
    first_name='Mike',
    last_name='Star',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729812014/MikeStar_yulapn.jpg'
    )

    dumb_and_dumber_artist5 = Artist(
    first_name='Karen',
    last_name='Duffy',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729811987/KarenDuffy_yaoktj.jpg'
    )

# Director for "Dumb and Dumber"
    dumb_and_dumber_director = Artist(
    first_name='Peter',
    last_name='Farrelly',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729812008/PeterFarrelly_rglejl.jpg'
    )

# Add artists to the database
    dumb_and_dumber_artists = [dumb_and_dumber_artist1, dumb_and_dumber_artist2, dumb_and_dumber_artist3, dumb_and_dumber_artist4, dumb_and_dumber_artist5,dumb_and_dumber_director]
    for person in dumb_and_dumber_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Dumb and Dumber"
    dumb_and_dumber_crew1 = crew.insert().values(
    artist_id=dumb_and_dumber_artist1.id,
    movie_id=29,  # Dumb and Dumber movie ID
    role='Actor',
    played='Lloyd Christmas'
    )

    dumb_and_dumber_crew2 = crew.insert().values(
    artist_id=dumb_and_dumber_artist2.id,
    movie_id=29,
    role='Actor',
    played='Harry Dunne'
    )

    dumb_and_dumber_crew3 = crew.insert().values(
    artist_id=dumb_and_dumber_artist3.id,
    movie_id=29,
    role='Actor',
    played='Mary Swanson'
    )

    dumb_and_dumber_crew4 = crew.insert().values(
    artist_id=dumb_and_dumber_artist4.id,
    movie_id=29,
    role='Actor',
    played='Joe Mentalino'
    )

    dumb_and_dumber_crew5 = crew.insert().values(
    artist_id=dumb_and_dumber_artist5.id,
    movie_id=29,
    role='Actor',
    played='J.P. Shay'
    )

    dumb_and_dumber_crew6 = crew.insert().values(
    artist_id=dumb_and_dumber_director.id,
    movie_id=29,
    role='Director'
    )

# Add crew entries to the database
    dumb_and_dumber_crew = [dumb_and_dumber_crew1, dumb_and_dumber_crew2, dumb_and_dumber_crew3, dumb_and_dumber_crew4, dumb_and_dumber_crew5, dumb_and_dumber_crew6]
    for person in dumb_and_dumber_crew:
        db.session.execute(person)
    db.session.commit()


# Artists for "21 Jump Street"
    jump_street_artist1 = Artist.query.filter_by(
    first_name='Jonah',
    last_name='Hill').first()


    jump_street_artist2 = Artist(
    first_name='Channing',
    last_name='Tatum',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813235/ChanningTatum_wblfqx.jpg'
    )

    jump_street_artist3 = Artist(
    first_name='Ice',
    last_name='Cube',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813252/IceCube_mgopnl.webp'
    )

    jump_street_artist4 = Artist(
    first_name='Brie',
    last_name='Larson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813232/BrieLarson_bgwevs.jpg'
    )

    jump_street_artist5 = Artist(
    first_name='Dave',
    last_name='Franco',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813240/Dave_Franco.PNG_qemuok.webp'
    )

# Director for "21 Jump Street"
    jump_street_director = Artist(
    first_name='Phil',
    last_name='Lord',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813267/Phil_Lord_osyy5a.jpg'
    )

# Add artists to the database
    jump_street_artists = [jump_street_artist1, jump_street_artist2, jump_street_artist3, jump_street_artist4, jump_street_artist5,jump_street_director]
    for person in jump_street_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "21 Jump Street"
    jump_street_crew1 = crew.insert().values(
    artist_id=jump_street_artist1.id,
    movie_id=30,  # 21 Jump Street movie ID
    role='Actor',
    played='Morton Schmidt'
    )

    jump_street_crew2 = crew.insert().values(
    artist_id=jump_street_artist2.id,
    movie_id=30,
    role='Actor',
    played='Greg Jenko'
    )

    jump_street_crew3 = crew.insert().values(
    artist_id=jump_street_artist3.id,
    movie_id=30,
    role='Actor',
    played='Captain Dickson'
    )

    jump_street_crew4 = crew.insert().values(
    artist_id=jump_street_artist4.id,
    movie_id=30,
    role='Actor',
    played='Molly'
    )

    jump_street_crew5 = crew.insert().values(
    artist_id=jump_street_artist5.id,
    movie_id=30,
    role='Actor',
    played='Eric'
    )

    jump_street_crew6 = crew.insert().values(
    artist_id=jump_street_director.id,
    movie_id=30,
    role='Director'
    )

# Add crew entries to the database
    jump_street_crew = [jump_street_crew1, jump_street_crew2, jump_street_crew3, jump_street_crew4, jump_street_crew5, jump_street_crew6]
    for person in jump_street_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "The 40-Year-Old Virgin"
    virgin_artist1 = Artist(
    first_name='Steve',
    last_name='Carell',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813677/SteveCarell_jswczx.jpg'
    )

    virgin_artist2 = Artist(
    first_name='Catherine',
    last_name='Keener',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813685/CatherineKeener_twh4oe.jpg'
    )

    virgin_artist3 = Artist.query.filter_by(
    first_name='Paul',
    last_name='Rudd').first()


    virgin_artist4 = Artist(
    first_name='Romany',
    last_name='Malco',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813669/Romany_Malco_by_David_Shankbone_ojgptp.jpg'
    )

    virgin_artist5 = Artist.query.filter_by(
    first_name='Seth',
    last_name='Rogen').first()

# Director for "The 40-Year-Old Virgin"
    virgin_director = Artist(
    first_name='Judd',
    last_name='Apatow',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729813660/JuddApatow_adp391.jpg'
    )

# Add artists to the database
    virgin_artists = [virgin_artist1, virgin_artist2, virgin_artist3, virgin_artist4, virgin_artist5,virgin_director]
    for person in virgin_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The 40-Year-Old Virgin"
    virgin_crew1 = crew.insert().values(
    artist_id=virgin_artist1.id,
    movie_id=31,  # The 40-Year-Old Virgin movie ID
    role='Actor',
    played='Andy Stitzer'
    )

    virgin_crew2 = crew.insert().values(
    artist_id=virgin_artist2.id,
    movie_id=31,
    role='Actor',
    played='Trish'
    )

    virgin_crew3 = crew.insert().values(
    artist_id=virgin_artist3.id,
    movie_id=31,
    role='Actor',
    played='David'
    )

    virgin_crew4 = crew.insert().values(
    artist_id=virgin_artist4.id,
    movie_id=31,
    role='Actor',
    played='Jay'
    )

    virgin_crew5 = crew.insert().values(
    artist_id=virgin_artist5.id,
    movie_id=31,
    role='Actor',
    played='Cal'
    )

    virgin_crew6 = crew.insert().values(
    artist_id=virgin_director.id,
    movie_id=31,
    role='Director'
    )

# Add crew entries to the database
    virgin_crew = [virgin_crew1, virgin_crew2, virgin_crew3, virgin_crew4, virgin_crew5, virgin_crew6]
    for person in virgin_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "Zoolander"
    zoolander_artist1 = Artist(
    first_name='Ben',
    last_name='Stiller',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814333/BenStiller_hdbmzv.jpg')


    zoolander_artist2 = Artist.query.filter_by(
    first_name='Owen',
    last_name='Wilson',
    ).first()

    zoolander_artist3 = Artist.query.filter_by(
    first_name='Will',
    last_name='Ferrell',
    ).first()

    zoolander_artist4 = Artist(
    first_name='Christine',
    last_name='Taylor',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814120/Christine_Taylor_hqml1d.webp'
    )

    zoolander_artist5 = Artist(
    first_name='Jon',
    last_name='Voight',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729814127/Jon_Voight_2011_zbxy0u.jpg'
    )



# Add artists to the database
    zoolander_artists = [zoolander_artist1,zoolander_artist4, zoolander_artist5]
    for person in zoolander_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Zoolander"
    zoolander_crew1 = crew.insert().values(
    artist_id=zoolander_artist1.id,
    movie_id=32,  # Zoolander movie ID
    role='Actor',
    played='Derek Zoolander'
    )

    zoolander_crew2 = crew.insert().values(
    artist_id=zoolander_artist2.id,
    movie_id=32,
    role='Actor',
    played='Hansel'
    )

    zoolander_crew3 = crew.insert().values(
    artist_id=zoolander_artist3.id,
    movie_id=32,
    role='Actor',
    played='Mugatu'
    )

    zoolander_crew4 = crew.insert().values(
    artist_id=zoolander_artist4.id,
    movie_id=32,
    role='Actor',
    played='Matilda Jeffries'
    )

    zoolander_crew5 = crew.insert().values(
    artist_id=zoolander_artist5.id,
    movie_id=32,
    role='Actor',
    played='Derek’s Father'
    )

    zoolander_crew6 = crew.insert().values(
    artist_id=zoolander_artist1.id,
    movie_id=32,
    role='Director'
    )

# Add crew entries to the database
    zoolander_crew = [zoolander_crew1, zoolander_crew2, zoolander_crew3, zoolander_crew4, zoolander_crew5, zoolander_crew6]
    for person in zoolander_crew:
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
