from app.models import db, Genre,Movie, environment, SCHEMA
from sqlalchemy.sql import text

def seed_movie_genres():
    action = Genre.query.filter_by(type='action').first()
    scifi = Genre.query.filter_by(type='scifi').first()
    romance = Genre.query.filter_by(type='romance').first()
    comedy = Genre.query.filter_by(type='comedy').first()
    horror = Genre.query.filter_by(type='horror').first()
    superhero = Genre.query.filter_by(type='superhero').first()
    drama = Genre.query.filter_by(type='drama').first()
    doc = Genre.query.filter_by(type='documentary').first()

    # random movie gernes
    movie1 = Movie.query.filter_by(title='The Exorcist: Believer').first()
    movie1.genres.append(horror)

    movie2 = Movie.query.filter_by(title='Killers of the Flower Moon').first()
    movie2.genres.append(horror)

    movie3 = Movie.query.filter_by(title='The Creator').first()
    movie3.genres.append(scifi)
    movie3.genres.append(action)

    movie4 = Movie.query.filter_by(title='A Haunting in Venice').first()
    movie4.genres.append(horror)

    movie5 = Movie.query.filter_by(title='Dumb Money').first()
    movie5.genres.append(comedy)
    movie5.genres.append(drama)

    movie6 = Movie.query.filter_by(title='Blue Beetle').first()
    movie6.genres.append(superhero)
    movie6.genres.append(action)

    movie7 = Movie.query.filter_by(title='Gran Turismo').first()
    movie7.genres.append(action)
    movie7.genres.append(drama)

    movie8 = Movie.query.filter_by(title='Haunted Mansion').first()
    movie8.genres.append(horror)


    movie9 = Movie.query.filter_by(title='Barbie').first()
    movie9.genres.append(comedy)

    movie10 = Movie.query.filter_by(title='Oppenheimer').first()
    movie10.genres.append(drama)
    movie10.genres.append(doc)
    # new movies genres
    movie11 = Movie.query.filter_by(title='Transformers: One').first()
    movie11.genres.append(scifi)
    movie11.genres.append(action)

    movie12 = Movie.query.filter_by(title='Beetlejuice 2').first()
    movie12.genres.append(horror)
    movie12.genres.append(comedy)

    movie13 = Movie.query.filter_by(title='The Beekeeper').first()
    movie13.genres.append(action)

    movie14 = Movie.query.filter_by(title='The Book of Clarence').first()
    movie14.genres.append(comedy)
    movie14.genres.append(drama)

    movie15 = Movie.query.filter_by(title='Freud\'s Last Session').first()
    movie15.genres.append(drama)

    movie16 = Movie.query.filter_by(title='Argylle').first()
    movie16.genres.append(action)
    movie16.genres.append(comedy)

    movie17 = Movie.query.filter_by(title='Lisa Frankenstein').first()
    movie17.genres.append(horror)

    movie18 = Movie.query.filter_by(title='Bob Marley: One Love').first()
    movie18.genres.append(drama)

    movie19 = Movie.query.filter_by(title='Kung Fu Panda 4').first()
    movie19.genres.append(comedy)
    movie19.genres.append(action)

    movie20 = Movie.query.filter_by(title='Ghostbusters: Frozen Empire').first()
    movie20.genres.append(comedy)
    movie20.genres.append(horror)

    movie21 = Movie.query.filter_by(title='Godzilla x Kong: The New Empire').first()
    movie21.genres.append(action)

    movie22 = Movie.query.filter_by(title='Sonic the Hedgehog 3').first()
    movie22.genres.append(comedy)
    movie22.genres.append(action)
    # comedy movies genres

    movie24 = Movie.query.filter_by(title='Superbad').first()
    movie24.genres.append(comedy)


    movie25 = Movie.query.filter_by(title='The Hangover').first()
    movie25.genres.append(comedy)


    movie26 = Movie.query.filter_by(title='Bridesmaids').first()
    movie26.genres.append(comedy)


    movie27 = Movie.query.filter_by(title='Step Brothers').first()
    movie27.genres.append(comedy)


    movie28 = Movie.query.filter_by(title='Groundhog Day').first()
    movie28.genres.append(comedy)


    movie29 = Movie.query.filter_by(title='Mean Girls').first()
    movie29.genres.append(comedy)



    movie30 = Movie.query.filter_by(title='Dumb and Dumber').first()
    movie30.genres.append(comedy)


    movie31 = Movie.query.filter_by(title='21 Jump Street').first()
    movie31.genres.append(comedy)


    movie32 = Movie.query.filter_by(title='The 40-Year-Old Virgin').first()
    movie32.genres.append(comedy)


    movie33 = Movie.query.filter_by(title='Zoolander').first()
    movie33.genres.append(comedy)

    # horror movies genres
    movie34 = Movie.query.filter_by(title='Hereditary').first()
    movie34.genres.append(horror)

    movie35 = Movie.query.filter_by(title='Get Out').first()
    movie35.genres.append(horror)

    movie36 = Movie.query.filter_by(title='A Quiet Place').first()
    movie36.genres.append(horror)

    movie37 = Movie.query.filter_by(title='The Conjuring').first()
    movie37.genres.append(horror)

    movie38 = Movie.query.filter_by(title='It Follows').first()
    movie38.genres.append(horror)

    movie39 = Movie.query.filter_by(title='Midsommar').first()
    movie39.genres.append(horror)

    movie40 = Movie.query.filter_by(title='The Witch').first()
    movie40.genres.append(horror)

    movie41 = Movie.query.filter_by(title='Us').first()
    movie41.genres.append(horror)

    movie42 = Movie.query.filter_by(title='Sinister').first()
    movie42.genres.append(horror)

    movie43 = Movie.query.filter_by(title='The Babadook').first()
    movie43.genres.append(horror)


    # romance genre

    movie44 = Movie.query.filter_by(title='The Notebook').first()
    movie44.genres.append(romance)

    movie45 = Movie.query.filter_by(title='Pride and Prejudice').first()
    movie45.genres.append(romance)

    movie46 = Movie.query.filter_by(title='La La Land').first()
    movie46.genres.append(romance)

    movie47 = Movie.query.filter_by(title='A Walk to Remember').first()
    movie47.genres.append(romance)

    movie48 = Movie.query.filter_by(title='Titanic').first()
    movie48.genres.append(romance)

    movie49 = Movie.query.filter_by(title='Crazy, Stupid, Love').first()
    movie49.genres.append(romance)

    movie50 = Movie.query.filter_by(title='The Fault in Our Stars').first()
    movie50.genres.append(romance)

    movie51 = Movie.query.filter_by(title='10 Things I Hate About You').first()
    movie51.genres.append(romance)

    movie52 = Movie.query.filter_by(title='Notting Hill').first()
    movie52.genres.append(romance)

    movie53 = Movie.query.filter_by(title='When Harry Met Sally...').first()
    movie53.genres.append(romance)


    # scifi genre
    movie54 = Movie.query.filter_by(title='Inception').first()
    movie54.genres.append(scifi)

    movie55 = Movie.query.filter_by(title='Blade Runner 2049').first()
    movie55.genres.append(scifi)

    movie56 = Movie.query.filter_by(title='The Matrix').first()
    movie56.genres.append(scifi)

    movie57 = Movie.query.filter_by(title='Interstellar').first()
    movie57.genres.append(scifi)

    movie58 = Movie.query.filter_by(title='Star Wars: Episode IV - A New Hope').first()
    movie58.genres.append(scifi)

    movie59 = Movie.query.filter_by(title='Arrival').first()
    movie59.genres.append(scifi)

    movie60 = Movie.query.filter_by(title='Ex Machina').first()
    movie60.genres.append(scifi)

    movie61 = Movie.query.filter_by(title='The Fifth Element').first()
    movie61.genres.append(scifi)

    movie62 = Movie.query.filter_by(title='Dune').first()
    movie62.genres.append(scifi)

    movie63 = Movie.query.filter_by(title='Eternal Sunshine of the Spotless Mind').first()
    movie63.genres.append(scifi)

    # action movies

    movie64 = Movie.query.filter_by(title='Mad Max: Fury Road').first()
    movie64.genres.append(action)

    movie65 = Movie.query.filter_by(title='John Wick').first()
    movie65.genres.append(action)

    movie66 = Movie.query.filter_by(title='Die Hard').first()
    movie66.genres.append(action)

    movie67 = Movie.query.filter_by(title='The Dark Knight').first()
    movie67.genres.append(action)
    movie67.genres.append(superhero)

    movie68 = Movie.query.filter_by(title='Gladiator').first()
    movie68.genres.append(action)

    movie69 = Movie.query.filter_by(title='The Avengers').first()
    movie69.genres.append(action)
    movie69.genres.append(superhero)

    movie70 = Movie.query.filter_by(title='Transformers').first()
    movie70.genres.append(action)

    movie71 = Movie.query.filter_by(title='Casino Royale').first()
    movie71.genres.append(action)

    movie72 = Movie.query.filter_by(title='Mission: Impossible - Fallout').first()
    movie72.genres.append(action)


    db.session.commit()

def undo_movie_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movie_genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM movie_genres"))

    db.session.commit()
