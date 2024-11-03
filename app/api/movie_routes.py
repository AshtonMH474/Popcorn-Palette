from flask import Blueprint, jsonify,request
from flask_login import login_required
from app.models import User,Movie,db,Movie_Image,Genre
from datetime import date

movie_routes = Blueprint('movies',__name__)

@movie_routes.route('/')
def all_movies():
    """
    Query for all movies
    """

    movies = Movie.query.all()
    return {'movies':[movie.to_dict() for movie in movies]}


@movie_routes.route('/<int:movie_id>')
def movie_details(movie_id):
    """
    Query for certain movie
    """
    movie = Movie.query.filter_by(id=movie_id).first()
    if movie is None:
        return {'errors': {'message': 'Movie Not Found'}}, 404
    return {'movie':movie.to_dict()}


@movie_routes.route('/search')
def search_movie():

    search_term = request.args.get('query',None)

    if not search_term:
        movies = Movie.query.all()

    else:
        movies = Movie.query.filter(Movie.title.ilike(f'%{search_term}%')).all()

    return {'movies': [movie.to_dict() for movie in movies]}


@movie_routes.route('/',methods=['POST'])
def check_movie():
    data = request.json

    movie_id = data.get('id')
    movie=Movie.query.filter_by(id=movie_id).first()

    if movie is None:
        release_date= data.get('releaseDate').split('-')

        title = data.get('title')
        id = data.get('id')
        description = data.get('description')
        movie_images = data.get('movieImages')
        genres = data.get('genres')



        # print('genres ---------------------------',genres)
        # return

        movie = Movie(id=id,title=title,description=description,custom=False,release_date=date(int(release_date[0]),int(release_date[1]),int(release_date[2])))
        db.session.add(movie)
        db.session.commit()
        movie_image = Movie_Image(movie_id = movie.id, img_url=movie_images[0]['imgUrl'],poster=movie_images[0]['poster'])
        db.session.add(movie_image)
        db.session.commit()

        for genre in genres:
                    curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    if curr_genre is None:
                        genre1 = Genre(type=genre['type'])
                        db.session.add(genre1)
                        db.session.commit()
                    curr_genre = Genre.query.filter_by(type=genre['type']).first()
                    movie.genres.append(curr_genre)
        db.session.commit()
        return jsonify({'movies':movie.to_dict()}),201

    else:
        return jsonify({'movies':'movie in db'})
