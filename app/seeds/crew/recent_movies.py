from app.models import db, Artist, environment, SCHEMA
from app.models.artist import crew
from sqlalchemy.sql import text

def seed_recent_movie_artists():
    # Artists for "Transformers: One" (2024)
    transformers_artist1 = Artist(
    first_name='Brian',
    last_name='Tyree Henry',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647826/Brian_Tyree_Henry_by_Gage_Skidmore_2_ouulql.jpg'
    )

    transformers_artist2 = Artist(
    first_name='Chris',
    last_name='Hemsworth',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647829/ChirsHimesowrth_xbtolt.webp'
    )

    transformers_artist3 = Artist(
    first_name='Scarlett',
    last_name='Johansson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647844/ScarlettJohanson_othjao.jpg'
    )

    transformers_artist4 = Artist(
    first_name='Keegan-Michael',
    last_name='Key',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647836/Key_ntestl.jpg'
    )

    transformers_artist5 = Artist(
    first_name='Laurence',
    last_name='Fishburne',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647839/LaurenceFishburnew_db0zm3.jpg'
    )

# Director for "Transformers: One" (2024)
    transformers_director = Artist(
    first_name='Josh',
    last_name='Cooley',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729647906/Josh_Cooley_by_Gage_Skidmore_hi3ccq.jpg'
    )

# Add artists to the database
    transformers_artists = [transformers_artist1, transformers_artist2, transformers_artist3, transformers_artist4, transformers_artist5,transformers_director]
    for person in transformers_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Transformers: One" (2024)
    transformers_crew1 = crew.insert().values(
    artist_id=transformers_artist1.id,
    movie_id=11,  # Replace with actual movie ID
    role='Actor',
    played='Megatron'
    )

    transformers_crew2 = crew.insert().values(
    artist_id=transformers_artist2.id,
    movie_id=11,
    role='Actor',
    played='Optimus Prime'
    )

    transformers_crew3 = crew.insert().values(
    artist_id=transformers_artist3.id,
    movie_id=11,
    role='Actor',
    played='Elita-1'  # Update character name as needed
    )

    transformers_crew4 = crew.insert().values(
    artist_id=transformers_artist4.id,
    movie_id=11,
    role='Actor',
    played='BumbleBee'  # Update character name as needed
    )

    transformers_crew5 = crew.insert().values(
    artist_id=transformers_artist5.id,
    movie_id=11,
    role='Actor',
    played='Alpha Trion'  # Update character name as needed
    )

    transformers_crew6 = crew.insert().values(
    artist_id=transformers_director.id,
    movie_id=11,
    role='Director'
    )

# Add crew entries to the database
    transformers_crew = [transformers_crew1, transformers_crew2, transformers_crew3, transformers_crew4, transformers_crew5, transformers_crew6]
    for person in transformers_crew:
        db.session.execute(person)
    db.session.commit()



    # Artists for "Beetlejuice 2"
    beetlejuice_artist1 = Artist(
    first_name='Michael',
    last_name='Keaton',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648607/MichaelKeaton_rp6qck.jpg'
    )

    beetlejuice_artist2 = Artist(
    first_name='Winona',
    last_name='Ryder',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648596/WinonaRyder_iqnfd4.jpg'
    )

    beetlejuice_artist3 = Artist(
    first_name='Jenna',
    last_name='Ortega',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648603/Jenna_Ortega-63792__cropped_dlbega.jpg'
    )

    beetlejuice_artist4 = Artist(
    first_name='Justin',
    last_name='Theroux',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648612/JustinTheroux_bqe3zr.webp'
    )

    beetlejuice_artist5 = Artist(
    first_name='Catherine',
    last_name="O'Hara",
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648586/Catherine_O_Hara-63919__cropped_2_wfb848.jpg'
    )

# Director for "Beetlejuice 2"
    beetlejuice_director = Artist(
    first_name='Tim',
    last_name='Burton',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729648592/Tim-Burton-2010.jpg_g8sugg.webp'
    )

# Add artists to the database
    beetlejuice_artists = [beetlejuice_artist1, beetlejuice_artist2, beetlejuice_artist3, beetlejuice_artist4, beetlejuice_artist5,beetlejuice_director]
    for person in beetlejuice_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Beetlejuice 2"
    beetlejuice_crew1 = crew.insert().values(
    artist_id=beetlejuice_artist1.id,
    movie_id=12,  # Beetlejuice 2 movie ID
    role='Actor',
    played='Beetlejuice'
    )

    beetlejuice_crew2 = crew.insert().values(
    artist_id=beetlejuice_artist2.id,
    movie_id=12,
    role='Actor',
    played='Lydia Deetz'
    )

    beetlejuice_crew3 = crew.insert().values(
    artist_id=beetlejuice_artist3.id,
    movie_id=12,
    role='Actor',
    played='Astrid Deetz'  # Update character name as needed
    )

    beetlejuice_crew4 = crew.insert().values(
    artist_id=beetlejuice_artist4.id,
    movie_id=12,
    role='Actor',
    played='Rory'  # Update character name as needed
    )

    beetlejuice_crew5 = crew.insert().values(
    artist_id=beetlejuice_artist5.id,
    movie_id=12,
    role='Actor',
    played='Delia Deetz'
    )

    beetlejuice_crew6 = crew.insert().values(
    artist_id=beetlejuice_director.id,
    movie_id=12,
    role='Director'
    )

# Add crew entries to the database
    beetlejuice_crew = [beetlejuice_crew1, beetlejuice_crew2, beetlejuice_crew3, beetlejuice_crew4, beetlejuice_crew5, beetlejuice_crew6]
    for person in beetlejuice_crew:
        db.session.execute(person)
    db.session.commit()

    # Artists for "The Beekeeper"
    beekeeper_artist1 = Artist(
    first_name='Jason',
    last_name='Statham',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729721063/JasonStatham_wmyfuy.jpg'
    )

    beekeeper_artist2 = Artist(
    first_name='Jeremy',
    last_name='Irons',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729720994/Jeremy_Irons_tefbno.jpg'
    )

    beekeeper_artist3 = Artist(
    first_name='Josh',
    last_name='Hutcherson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729721052/JoshHutcherson_diyc7i.jpg'
    )

    beekeeper_artist4 = Artist(
    first_name='Taylor',
    last_name='James',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729720944/TaylorJames_xy6qkl.jpg'
    )

    beekeeper_artist5 = Artist(
    first_name='Jemma',
    last_name='Redgrave',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729721006/JemmaRedgrave_ilsjl0.jpg'
    )

# Director for "The Beekeeper"
    beekeeper_director = Artist(
    first_name='David',
    last_name='Klein',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729721174/DavidAyer_g9pp7u.jpg'
    )

# Add artists to the database
    beekeeper_artists = [beekeeper_artist1, beekeeper_artist2, beekeeper_artist3, beekeeper_artist4, beekeeper_artist5,beekeeper_director]
    for person in beekeeper_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The Beekeeper"
    beekeeper_crew1 = crew.insert().values(
    artist_id=beekeeper_artist1.id,
    movie_id=13,  # The Beekeeper movie ID
    role='Actor',
    played='Adam Clay'
    )

    beekeeper_crew2 = crew.insert().values(
    artist_id=beekeeper_artist2.id,
    movie_id=13,
    role='Actor',
    played='Wallace Westwyld'  # Update character name as needed
    )

    beekeeper_crew3 = crew.insert().values(
    artist_id=beekeeper_artist3.id,
    movie_id=13,
    role='Actor',
    played='Derek Danforth'  # Update character name as needed
    )

    beekeeper_crew4 = crew.insert().values(
    artist_id=beekeeper_artist4.id,
    movie_id=13,
    role='Actor',
    played='Lazarus'  # Update character name as needed
    )

    beekeeper_crew5 = crew.insert().values(
    artist_id=beekeeper_artist5.id,
    movie_id=13,
    role='Actor',
    played='Jessica Danforth'  # Update character name as needed
    )

    beekeeper_crew6 = crew.insert().values(
    artist_id=beekeeper_director.id,
    movie_id=13,
    role='Director'
    )

# Add crew entries to the database
    beekeeper_crew = [beekeeper_crew1, beekeeper_crew2, beekeeper_crew3, beekeeper_crew4, beekeeper_crew5, beekeeper_crew6]
    for person in beekeeper_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "The Book of Clarence"
    clarence_artist1 = Artist.query.filter_by(first_name='LaKeith',last_name='Stanfield').first()

    clarence_artist2 = Artist(
    first_name='RJ',
    last_name='Cyler',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729722056/Rj_y8ptde.jpg'
    )

    clarence_artist3 = Artist(
    first_name='Caleb',
    last_name='McLaughlin',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729722039/CalebMcLaughlin_nqahxl.jpg'
    )

    clarence_artist4 = Artist(
    first_name='Anna',
    last_name='Diop',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729722045/AnnaDiop_jl19pw.jpg'
    )

    clarence_artist5 = Artist(
    first_name='James',
    last_name='McAvoy',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729722069/JamesMcAvoy_yewo95.jpg'
    )

# Director for "The Book of Clarence"
    clarence_director = Artist(
    first_name='Jeymes',
    last_name='Samuel',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729722087/Jeymes_f1cuzm.webp'
    )

# Add artists to the database
    clarence_artists = [clarence_artist1, clarence_artist2, clarence_artist3, clarence_artist4, clarence_artist5,clarence_director]
    for person in clarence_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "The Book of Clarence"
    clarence_crew1 = crew.insert().values(
    artist_id=clarence_artist1.id,
    movie_id=14,  # The Book of Clarence movie ID
    role='Actor',
    played='Clarence'
    )

    clarence_crew2 = crew.insert().values(
    artist_id=clarence_artist2.id,
    movie_id=14,
    role='Actor',
    played='Elijah'  # Update character name as needed
    )

    clarence_crew3 = crew.insert().values(
    artist_id=clarence_artist3.id,
    movie_id=14,
    role='Actor',
    played='Dirty Zeke'  # Update character name as needed
    )

    clarence_crew4 = crew.insert().values(
    artist_id=clarence_artist4.id,
    movie_id=14,
    role='Actor',
    played='Varinia'  # Update character name as needed
    )

    clarence_crew5 = crew.insert().values(
    artist_id=clarence_artist5.id,
    movie_id=14,
    role='Actor',
    played='James McAvoy'  # Update character name as needed
    )

    clarence_crew6 = crew.insert().values(
    artist_id=clarence_director.id,
    movie_id=14,
    role='Director'
    )

# Add crew entries to the database
    clarence_crew = [clarence_crew1, clarence_crew2, clarence_crew3, clarence_crew4, clarence_crew5, clarence_crew6]
    for person in clarence_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Freud's Last Session"
    freud_artist1 = Artist(
    first_name='Matthew',
    last_name='Goode',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723354/Matthew_Goode_gnvyql.webp'
    )

    freud_artist2 = Artist(
    first_name='Anthony',
    last_name='Hopkins',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723269/Anthony-Hopkins_pouok9.webp'
    )

    freud_artist3 = Artist(
    first_name='Liv',
    last_name='Lisa Fries',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723325/LivLisaFries_ibcbta.jpg'
    )

    freud_artist4 = Artist(
    first_name='Jermey',
    last_name='Northam',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723290/Jeremy_Northam__cropped_xhq1b0.jpg'
    )

    freud_artist5 = Artist(
    first_name='Jodi',
    last_name='Balfour',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723283/JodiBalfour_xgfonh.jpg'
    )

# Director for "Freud's Last Session"
    freud_director = Artist(
    first_name='Matt',
    last_name='Brown',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729723339/MattBrown_koxvwq.jpg'
    )

# Add artists to the database
    freud_artists = [freud_artist1, freud_artist2, freud_artist3, freud_artist4, freud_artist5,freud_director]
    for person in freud_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Freud's Last Session"
    freud_crew1 = crew.insert().values(
    artist_id=freud_artist1.id,
    movie_id=15,  # Freud's Last Session movie ID
    role='Actor',
    played='C.S. Lewis'
    )

    freud_crew2 = crew.insert().values(
    artist_id=freud_artist2.id,
    movie_id=15,
    role='Actor',
    played='Sigmund Freud'
    )

    freud_crew3 = crew.insert().values(
    artist_id=freud_artist3.id,
    movie_id=15,
    role='Actor',
    played='Anna Freud'
    )

    freud_crew4 = crew.insert().values(
    artist_id=freud_artist4.id,
    movie_id=15,
    role='Actor',
    played='Carl Jung'  # Update character name as needed
    )

    freud_crew5 = crew.insert().values(
    artist_id=freud_artist5.id,
    movie_id=15,
    role='Actor',
    played='Dorothy Burlingham'  # Update character name as needed
    )

    freud_crew6 = crew.insert().values(
    artist_id=freud_director.id,
    movie_id=15,
    role='Director'
    )

# Add crew entries to the database
    freud_crew = [freud_crew1, freud_crew2, freud_crew3, freud_crew4, freud_crew5, freud_crew6]
    for person in freud_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Argylle"
    argylle_artist1 = Artist(
    first_name='Henry',
    last_name='Cavill',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724522/Henry_Cavill_tyivwd.webp'
    )

    argylle_artist2 = Artist(
    first_name='Bryce',
    last_name='Dallas Howard',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724508/BryceDallasHoward_igbrxw.jpg'
    )

    argylle_artist3 = Artist(
    first_name='Samuel',
    last_name='L. Jackson',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724555/Samuel_L._Jackson_stdqpy.jpg'
    )

    argylle_artist4 = Artist(
    first_name='John',
    last_name='Cena',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724529/JohnCena_esjj0e.jpg'
    )

    argylle_artist5 = Artist(
    first_name='Dua',
    last_name='Lipa',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724516/DuaLipa_imwyg0.jpg'
    )

# Director for "Argylle"
    argylle_director = Artist(
    first_name='Matthew',
    last_name='Vaughn',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729724546/MAtthewVaughn_nfbqmo.jpg'
    )

# Add artists to the database
    argylle_artists = [argylle_artist1, argylle_artist2, argylle_artist3, argylle_artist4, argylle_artist5,argylle_director]
    for person in argylle_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Argylle"
    argylle_crew1 = crew.insert().values(
    artist_id=argylle_artist1.id,
    movie_id=16,  # Argylle movie ID
    role='Actor',
    played='Argylle'  # Update character name as needed
    )

    argylle_crew2 = crew.insert().values(
    artist_id=argylle_artist2.id,
    movie_id=16,
    role='Actor',
    played='Elly Conway'  # Update character name as needed
    )

    argylle_crew3 = crew.insert().values(
    artist_id=argylle_artist3.id,
    movie_id=16,
    role='Actor',
    played='Alfred Solomon'  # Update character name as needed
    )

    argylle_crew4 = crew.insert().values(
    artist_id=argylle_artist4.id,
    movie_id=16,
    role='Actor',
    played='Wyatt'  # Update character name as needed
    )

    argylle_crew5 = crew.insert().values(
    artist_id=argylle_artist5.id,
    movie_id=16,
    role='Actor',
    played='LaGrange'  # Update character name as needed
    )

    argylle_crew6 = crew.insert().values(
    artist_id=argylle_director.id,
    movie_id=16,
    role='Director'
    )

# Add crew entries to the database
    argylle_crew = [argylle_crew1, argylle_crew2, argylle_crew3, argylle_crew4, argylle_crew5, argylle_crew6]
    for person in argylle_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Lisa Frankenstein"
    lisa_frankenstein_artist1 = Artist(
    first_name='Kathryn',
    last_name='Newton',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725145/KathrynNewton_k0wzwo.jpg'
    )

    lisa_frankenstein_artist2 = Artist(
    first_name='Cole',
    last_name='Sprouse',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725121/ColeSprouse_vqwtdj.avif'
    )

    lisa_frankenstein_artist3 = Artist(
    first_name='Liza',
    last_name='Soberano',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725152/LizaSoberano_n6g3ff.jpg'
    )

    lisa_frankenstein_artist4 = Artist(
    first_name='Carla',
    last_name='Gugino',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725116/CarlaGugino_ujxbwf.jpg'
    )

    lisa_frankenstein_artist5 = Artist(
    first_name='Jenna',
    last_name='Davis',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725131/Jenna_Davis_mf9yyz.webp'
    )

# Director for "Lisa Frankenstein"
    lisa_frankenstein_director = Artist(
    first_name='Zelda',
    last_name='Williams',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729725160/ZeldaWilliams_luccyc.jpg'
    )

# Add artists to the database
    lisa_frankenstein_artists = [lisa_frankenstein_artist1, lisa_frankenstein_artist2, lisa_frankenstein_artist3, lisa_frankenstein_artist4, lisa_frankenstein_artist5,lisa_frankenstein_director]
    for person in lisa_frankenstein_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Lisa Frankenstein"
    lisa_frankenstein_crew1 = crew.insert().values(
    artist_id=lisa_frankenstein_artist1.id,
    movie_id=17,  # Lisa Frankenstein movie ID
    role='Actor',
    played='Lisa'
    )

    lisa_frankenstein_crew2 = crew.insert().values(
    artist_id=lisa_frankenstein_artist2.id,
    movie_id=17,
    role='Actor',
    played='The Creature'  # Update character name as needed
    )

    lisa_frankenstein_crew3 = crew.insert().values(
    artist_id=lisa_frankenstein_artist3.id,
    movie_id=17,
    role='Actor',
    played='Taffy'  # Update character name as needed
    )

    lisa_frankenstein_crew4 = crew.insert().values(
    artist_id=lisa_frankenstein_artist4.id,
    movie_id=17,
    role='Actor',
    played='Janet'  # Update character name as needed
    )

    lisa_frankenstein_crew5 = crew.insert().values(
    artist_id=lisa_frankenstein_artist5.id,
    movie_id=17,
    role='Actor',
    played='Lori'  # Update character name as needed
    )

    lisa_frankenstein_crew6 = crew.insert().values(
    artist_id=lisa_frankenstein_director.id,
    movie_id=17,
    role='Director'
    )

# Add crew entries to the database
    lisa_frankenstein_crew = [lisa_frankenstein_crew1, lisa_frankenstein_crew2, lisa_frankenstein_crew3, lisa_frankenstein_crew4, lisa_frankenstein_crew5, lisa_frankenstein_crew6]
    for person in lisa_frankenstein_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Bob Marley: One Love"
    bob_marley_artist1 = Artist(
    first_name='Kingsley',
    last_name='Ben-Adir',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727099/KingsleyBenAdir_gqjhmd.jpg'
    )

    bob_marley_artist2 = Artist(
    first_name='Lashana',
    last_name='Lynch',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727104/Lashanalynch_q0qqeu.webp'
    )

    bob_marley_artist3 = Artist(
    first_name='James',
    last_name='Norton',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727083/JamesNorton_eccgpc.jpg'
    )

    bob_marley_artist4 = Artist(
    first_name='Michael',
    last_name='Gandolfini',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727114/Michael_Gandolfini_gve2q7.webp'
    )

    bob_marley_artist5 = Artist(
    first_name='Tosin',
    last_name='Cole',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727125/Tosin_Cole_a619ng.webp'
    )

# Director for "Bob Marley: One Love"
    bob_marley_director = Artist(
    first_name='Reinaldo',
    last_name='Marcus Green',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727211/Reinalod_y5uot0.jpg'
    )

# Add artists to the database
    bob_marley_artists = [bob_marley_artist1, bob_marley_artist2, bob_marley_artist3, bob_marley_artist4, bob_marley_artist5,bob_marley_director]
    for person in bob_marley_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Bob Marley: One Love"
    bob_marley_crew1 = crew.insert().values(
    artist_id=bob_marley_artist1.id,
    movie_id=18,  # Bob Marley: One Love movie ID
    role='Actor',
    played='Bob Marley'
    )

    bob_marley_crew2 = crew.insert().values(
    artist_id=bob_marley_artist2.id,
    movie_id=18,
    role='Actor',
    played='Rita Marley'
    )

    bob_marley_crew3 = crew.insert().values(
    artist_id=bob_marley_artist3.id,
    movie_id=18,
    role='Actor',
    played='Chris Blackwell'  # Update character name as needed
    )

    bob_marley_crew4 = crew.insert().values(
    artist_id=bob_marley_artist4.id,
    movie_id=18,
    role='Actor',
    played='Howard Bloom'  # Update character name as needed
    )

    bob_marley_crew5 = crew.insert().values(
    artist_id=bob_marley_artist5.id,
    movie_id=18,
    role='Actor',
    played='Tyrone Downie'  # Update character name as needed
    )

    bob_marley_crew6 = crew.insert().values(
    artist_id=bob_marley_director.id,
    movie_id=18,
    role='Director'
    )

# Add crew entries to the database
    bob_marley_crew = [bob_marley_crew1, bob_marley_crew2, bob_marley_crew3, bob_marley_crew4, bob_marley_crew5, bob_marley_crew6]
    for person in bob_marley_crew:
        db.session.execute(person)
    db.session.commit()


    # Artists for "Kung Fu Panda 4"
    kung_fu_panda_artist1 = Artist(
    first_name='Jack',
    last_name='Black',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727692/JackBlack_h2rf3t.jpg'
    )

    kung_fu_panda_artist2 = Artist(
    first_name='Dustin',
    last_name='Hoffman',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727672/DustinHoffman_clqdzc.jpg'
    )

    kung_fu_panda_artist3 = Artist(
    first_name='Bryan',
    last_name='Cranston',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727662/BryanCranston_pwnitm.jpg'
    )

    kung_fu_panda_artist4 = Artist.query.filter_by(
    first_name='Seth',
    last_name='Rogen',
    ).first()

    kung_fu_panda_artist5 = Artist(
    first_name='Jackie',
    last_name='Chan',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727700/JackieChan_bv1yay.jpg'
    )

# Director for "Kung Fu Panda 4"
    kung_fu_panda_director = Artist(
    first_name='Mike',
    last_name='Mitchell',
    img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1729727731/MikeMitchell_u7lnpj.jpg'
    )

# Add artists to the database
    kung_fu_panda_artists = [kung_fu_panda_artist1, kung_fu_panda_artist2, kung_fu_panda_artist3, kung_fu_panda_artist4, kung_fu_panda_artist5,kung_fu_panda_director]
    for person in kung_fu_panda_artists:
        db.session.add(person)

    db.session.commit()

# Crew entries for "Kung Fu Panda 4"
    kung_fu_panda_crew1 = crew.insert().values(
    artist_id=kung_fu_panda_artist1.id,
    movie_id=19,  # Kung Fu Panda 4 movie ID
    role='Actor',
    played='Po'
    )

    kung_fu_panda_crew2 = crew.insert().values(
    artist_id=kung_fu_panda_artist2.id,
    movie_id=19,
    role='Actor',
    played='Master Shifu'
    )

    kung_fu_panda_crew3 = crew.insert().values(
    artist_id=kung_fu_panda_artist3.id,
    movie_id=19,
    role='Actor',
    played='Li Shan'
    )

    kung_fu_panda_crew4 = crew.insert().values(
    artist_id=kung_fu_panda_artist4.id,
    movie_id=19,
    role='Actor',
    played='Mantis'
    )

    kung_fu_panda_crew5 = crew.insert().values(
    artist_id=kung_fu_panda_artist5.id,
    movie_id=19,
    role='Actor',
    played='Monkey'
    )

    kung_fu_panda_crew6 = crew.insert().values(
    artist_id=kung_fu_panda_director.id,
    movie_id=19,
    role='Director'
    )

# Add crew entries to the database
    kung_fu_panda_crew = [kung_fu_panda_crew1, kung_fu_panda_crew2, kung_fu_panda_crew3, kung_fu_panda_crew4, kung_fu_panda_crew5, kung_fu_panda_crew6]
    for person in kung_fu_panda_crew:
        db.session.execute(person)
    db.session.commit()



def undo_recent_movie_artists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.artists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM artists"))

    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.crew RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM crew"))

    db.session.commit()
