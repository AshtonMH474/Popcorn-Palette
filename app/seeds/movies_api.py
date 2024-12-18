from app.models import db, Movie,Genre,Movie_Image, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date
import requests


api_key = '79009e38d3509a590d6510f6e91c4cd8'



def seed_api_movies():
    seed_now_playing()
    seed_movies_by_genre('Crime')
    seed_movies_by_genre('Action')
    seed_movies_by_genre('Science Fiction')
    seed_movies_by_genre('Horror')
    seed_movies_by_genre('Comedy')
    seed_watchlist_movies()


    db.session.commit()

def undo_api_movies():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.movies RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM movies"))

    db.session.commit()



def create_genres(genre_ids):
    url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US'
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        new_list = []

        for genre in data['genres']:
            if genre_ids and genre['id'] in genre_ids:
                obj = {
                'type': genre['name']
                }
                new_list.append(obj)

        return new_list


def seed_now_playing():
        page = 1
        url = f'https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&page={page}'

        response = requests.get(url)

        if response.status_code == 200:
            testRes = response.json()  # Parse the JSON response
            print(testRes['results'])

            for movie in testRes['results']:
                release_date = movie['release_date'].split('-')
                img = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                genres = create_genres(movie['genre_ids'])

                print('movie:---------------',movie)
                movie = Movie(id=movie['id'],description=movie['overview'],title=movie['title'],lang=movie['original_language'],for_home=True,release_date=date(int(release_date[0]),int(release_date[1]),int(release_date[2])))
                db.session.add(movie)
                db.session.commit()
                for genre in genres:
                    curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    if curr_genre is None:
                        genre1 = Genre(type=genre['type'])
                        db.session.add(genre1)
                        db.session.commit()
                    curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    movie.genres.append(curr_genre)

                movie_image = Movie_Image(movie_id=movie.id,img_url=img,poster=True)
                db.session.add(movie_image)
            db.session.commit()
        else:
            print(f'Error: {response.status_code} - {response.text}')


def seed_movies_by_genre(genre_name):
    base_url = 'https://api.themoviedb.org/3'

        # Fetch the list of movie genres
    response_genres = requests.get(f'{base_url}/genre/movie/list?api_key={api_key}&language=en-US')


    genre_data = response_genres.json()
    genres = genre_data['genres']

        # Find the genre object by name
    obj_genre = next((genre for genre in genres if genre['name'] == genre_name), None)

    if not obj_genre:
        print('Genre not found')
        return

        # Fetch movies for the found genre
    response_movies = requests.get(f'{base_url}/discover/movie?api_key={api_key}&with_genres={obj_genre["id"]}')


    movies_data = response_movies.json()

    for movie in movies_data['results']:

            has_movie = Movie.query.filter_by(id=movie['id']).first()
            if has_movie is None and len(movie['release_date']) > 0:
                release_date = movie['release_date'].split('-') if movie['release_date'] else []

                img = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
                genres = create_genres(movie['genre_ids'])

            # print('movie:---------------',movie)
                movie = Movie(id=movie['id'],description=movie['overview'],title=movie['title'],lang=movie['original_language'],for_home=True,release_date=date(int(release_date[0]),int(release_date[1]),int(release_date[2])))
                db.session.add(movie)
                db.session.commit()

                for genre in genres:
                    curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    if curr_genre is None:
                        genre1 = Genre(type=genre['type'])
                        db.session.add(genre1)
                        db.session.commit()
                        curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    movie.genres.append(curr_genre)

                movie_image = Movie_Image(movie_id=movie.id,img_url=img,poster=True)
                db.session.add(movie_image)
    db.session.commit()


def seed_watchlist_movies():
    page = 1
    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Star%20Wars%20IV&page={page}'
    response = requests.get(url)

    star_wars_data = response.json()
    star_wars = star_wars_data['results'][0]

    star_wars_release_date = star_wars['release_date'].split('-')
    star_wars_img = f"https://image.tmdb.org/t/p/w500{star_wars['poster_path']}"
    star_wars_genres = create_genres(star_wars['genre_ids'])
    star_wars_movie = Movie(id=star_wars['id'],description=star_wars['overview'],title=star_wars['title'],lang=star_wars['original_language'],for_home=True,release_date=date(int(star_wars_release_date[0]),int(star_wars_release_date[1]),int(star_wars_release_date[2])))


    db.session.add(star_wars_movie)
    db.session.commit()

    for genre in star_wars_genres:
        curr_genre = Genre.query.filter_by(type=genre['type']).first()
        if curr_genre is None:
            genre1 = Genre(type=genre['type'])
            db.session.add(genre1)
            db.session.commit()
        curr_genre = Genre.query.filter_by(type=genre['type']).first()
        star_wars_movie.genres.append(curr_genre)
    movie_image = Movie_Image(movie_id=star_wars_movie.id,img_url=star_wars_img,poster=True)
    db.session.add(movie_image)
    db.session.commit()


    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=The%20Dark%20Knight&page={page}'
    response = requests.get(url)

    batman_data = response.json()
    batman = batman_data['results'][0]

    foundMovie = Movie.query.filter_by(id=batman['id']).first()

    if foundMovie is None:

        batman_release_date = batman['release_date'].split('-')
        batman_img = f"https://image.tmdb.org/t/p/w500{batman['poster_path']}"
        batman_genres = create_genres(batman['genre_ids'])
        batman_movie = Movie(id=batman['id'],description=batman['overview'],lang=batman['original_language'],for_home=True,title=batman['title'],release_date=date(int(batman_release_date[0]),int(batman_release_date[1]),int(batman_release_date[2])))


        db.session.add(batman_movie)
        db.session.commit()

        for genre in batman_genres:
            curr_genre = Genre.query.filter_by(type=genre['type']).first()
            if curr_genre is None:
                genre1 = Genre(type=genre['type'])
                db.session.add(genre1)
                db.session.commit()
            curr_genre = Genre.query.filter_by(type=genre['type']).first()
            batman_movie.genres.append(curr_genre)
        movie_image = Movie_Image(movie_id=batman_movie.id,img_url=batman_img,poster=True)
        db.session.add(movie_image)
        db.session.commit()

    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=10%20Things%20I%20Hate%20About%20You&page={page}'
    response = requests.get(url)

# Ensure the request was successful
    if response.status_code == 200:
        ten_things_data = response.json()
        if ten_things_data['results']:  # Check if there are results
            ten_things_movie = ten_things_data['results'][0]

        # Process movie details
            ten_things_release_date = ten_things_movie['release_date'].split('-')
            ten_things_img_url = f"https://image.tmdb.org/t/p/w500{ten_things_movie['poster_path']}"
            ten_things_genres = create_genres(ten_things_movie['genre_ids'])

        # Create movie instance
            ten_things_movie_instance = Movie(
                id=ten_things_movie['id'],
                lang=ten_things_movie['original_language'],for_home=True,
                description=ten_things_movie['overview'],
                title=ten_things_movie['title'],
                release_date=date(int(ten_things_release_date[0]), int(ten_things_release_date[1]), int(ten_things_release_date[2]))
            )

            db.session.add(ten_things_movie_instance)
            db.session.commit()

        # Add genres
            for genre in ten_things_genres:
                curr_genre = Genre.query.filter_by(type=genre['type']).first()
                if curr_genre is None:
                    curr_genre = Genre(type=genre['type'])
                    db.session.add(curr_genre)
                    db.session.commit()
                ten_things_movie_instance.genres.append(curr_genre)

        # Add movie image
            ten_things_movie_image = Movie_Image(movie_id=ten_things_movie_instance.id, img_url=ten_things_img_url, poster=True)
            db.session.add(ten_things_movie_image)
            db.session.commit()


    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=A%20Quiet%20Place&page={page}&primary_release_year=2018'

    response = requests.get(url)

# Ensure the request was successful
    if response.status_code == 200:
        quiet_place_data = response.json()
        if quiet_place_data['results']:  # Check if there are results
            quiet_place_movie = quiet_place_data['results'][0]

        # Process movie details
            quiet_place_release_date = quiet_place_movie['release_date'].split('-')
            quiet_place_img_url = f"https://image.tmdb.org/t/p/w500{quiet_place_movie['poster_path']}"
            quiet_place_genres = create_genres(quiet_place_movie['genre_ids'])

        # Create movie instance
            quiet_place_movie_instance = Movie(
            id=quiet_place_movie['id'],
            lang=quiet_place_movie['original_language'],for_home=True,
            description=quiet_place_movie['overview'],
            title=quiet_place_movie['title'],
            release_date=date(int(quiet_place_release_date[0]), int(quiet_place_release_date[1]), int(quiet_place_release_date[2]))
            )

            db.session.add(quiet_place_movie_instance)
            db.session.commit()


            for genre in quiet_place_genres:
                curr_genre = Genre.query.filter_by(type=genre['type']).first()
                if curr_genre is None:
                    curr_genre = Genre(type=genre['type'])
                    db.session.add(curr_genre)
                    db.session.commit()
                quiet_place_movie_instance.genres.append(curr_genre)


            quiet_place_movie_image = Movie_Image(movie_id=quiet_place_movie_instance.id, img_url=quiet_place_img_url, poster=True)
            db.session.add(quiet_place_movie_image)
            db.session.commit()


    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=21%20Jump%20Street&page={page}'
    response = requests.get(url)

# Ensure the request was successful
    if response.status_code == 200:
        jump_street_data = response.json()
        if jump_street_data['results']:  # Check if there are results
            jump_street_movie = jump_street_data['results'][0]

        # Process movie details
            jump_street_release_date = jump_street_movie['release_date'].split('-')
            jump_street_img_url = f"https://image.tmdb.org/t/p/w500{jump_street_movie['poster_path']}"
            jump_street_genres = create_genres(jump_street_movie['genre_ids'])

        # Create movie instance
            jump_street_movie_instance = Movie(
            id=jump_street_movie['id'],
            lang=jump_street_movie['original_language'],for_home=True,
            description=jump_street_movie['overview'],
            title=jump_street_movie['title'],
            release_date=date(int(jump_street_release_date[0]), int(jump_street_release_date[1]), int(jump_street_release_date[2]))
            )

            db.session.add(jump_street_movie_instance)
            db.session.commit()

        # Add genres
            for genre in jump_street_genres:
                curr_genre = Genre.query.filter_by(type=genre['type']).first()
                if curr_genre is None:
                    curr_genre = Genre(type=genre['type'])
                    db.session.add(curr_genre)
                    db.session.commit()
                jump_street_movie_instance.genres.append(curr_genre)

        # Add movie image
            jump_street_movie_image = Movie_Image(movie_id=jump_street_movie_instance.id, img_url=jump_street_img_url, poster=True)
            db.session.add(jump_street_movie_image)
            db.session.commit()



    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Bob%20Marley%3A%20One%20Love&page={page}'
    response = requests.get(url)

# Ensure the request was successful
    if response.status_code == 200:
        bob_marley_data = response.json()
        if bob_marley_data['results']:  # Check if there are results
            bob_marley_movie = bob_marley_data['results'][0]

        # Process movie details
            bob_marley_release_date = bob_marley_movie['release_date'].split('-')
            bob_marley_img_url = f"https://image.tmdb.org/t/p/w500{bob_marley_movie['poster_path']}"
            bob_marley_genres = create_genres(bob_marley_movie['genre_ids'])

        # Create movie instance
            bob_marley_movie_instance = Movie(
            id=bob_marley_movie['id'],
            lang=bob_marley_movie['original_language'],for_home=True,
            description=bob_marley_movie['overview'],
            title=bob_marley_movie['title'],
            release_date=date(int(bob_marley_release_date[0]), int(bob_marley_release_date[1]), int(bob_marley_release_date[2]))
            )

            db.session.add(bob_marley_movie_instance)
            db.session.commit()

        # Add genres
            for genre in bob_marley_genres:
                curr_genre = Genre.query.filter_by(type=genre['type']).first()
                if curr_genre is None:
                    curr_genre = Genre(type=genre['type'])
                    db.session.add(curr_genre)
                    db.session.commit()
            bob_marley_movie_instance.genres.append(curr_genre)

        # Add movie image
            bob_marley_movie_image = Movie_Image(movie_id=bob_marley_movie_instance.id, img_url=bob_marley_img_url, poster=True)
            db.session.add(bob_marley_movie_image)
            db.session.commit()
    # url=f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Inside+Out+2&page={page}'
    # response = requests.get(url)

    # if response.status_code == 200:
    #     inside_out_data = response.json()
    #     if inside_out_data['results']:  # Check if there are results
    #         inside_movie = inside_out_data['results'][0]

    #         # Process movie details
    #         inside_release_date = inside_movie['release_date'].split('-')
    #         inside_img_url = f"https://image.tmdb.org/t/p/w500{inside_movie['poster_path']}"
    #         inside_genres = create_genres(inside_movie['genre_ids'])

    #     # Create movie instance
    #         inside_movie_instance = Movie(
    #             id=inside_movie['id'],
    #             lang=inside_movie['original_language'],for_home=True,
    #             description=inside_movie['overview'],
    #             title=inside_movie['title'],
    #             release_date=date(int(inside_release_date[0]), int(inside_release_date[1]), int(inside_release_date[2]))
    #         )

    #         db.session.add(inside_movie_instance)
    #         db.session.commit()

    #     # Add genres
    #         for genre in inside_genres:
    #             curr_genre = Genre.query.filter_by(type=genre['type']).first()
    #             if curr_genre is None:
    #                 curr_genre = Genre(type=genre['type'])
    #                 db.session.add(curr_genre)
    #                 db.session.commit()
    #         inside_movie_instance.genres.append(curr_genre)

    #     # Add movie image
    #         inside_movie_image = Movie_Image(movie_id=inside_movie_instance.id, img_url=inside_img_url, poster=True)
    #         db.session.add(inside_movie_image)
    #         db.session.commit()


    url = f'https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Oppenheimer&page={page}'
    response = requests.get(url)

# Ensure the request was successful
    if response.status_code == 200:
        oppenheimer_data = response.json()
        if oppenheimer_data['results']:  # Check if there are results
            oppenheimer_movie = oppenheimer_data['results'][0]

        # Process movie details
            oppenheimer_release_date = oppenheimer_movie['release_date'].split('-')
            oppenheimer_img_url = f"https://image.tmdb.org/t/p/w500{oppenheimer_movie['poster_path']}"
            oppenheimer_genres = create_genres(oppenheimer_movie['genre_ids'])

        # Create movie instance
            oppenheimer_movie_instance = Movie(
                id=oppenheimer_movie['id'],
                lang=oppenheimer_movie['original_language'],for_home=True,
                description=oppenheimer_movie['overview'],
                title=oppenheimer_movie['title'],
                release_date=date(int(oppenheimer_release_date[0]), int(oppenheimer_release_date[1]), int(oppenheimer_release_date[2]))
            )

            db.session.add(oppenheimer_movie_instance)
            db.session.commit()

        # Add genres
            for genre in oppenheimer_genres:
                curr_genre = Genre.query.filter_by(type=genre['type']).first()
                if curr_genre is None:
                    curr_genre = Genre(type=genre['type'])
                    db.session.add(curr_genre)
                    db.session.commit()
            oppenheimer_movie_instance.genres.append(curr_genre)

        # Add movie image
            oppenheimer_movie_image = Movie_Image(movie_id=oppenheimer_movie_instance.id, img_url=oppenheimer_img_url, poster=True)
            db.session.add(oppenheimer_movie_image)
            db.session.commit()
