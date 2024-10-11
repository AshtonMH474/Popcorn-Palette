from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User,Movie

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
     return {'movie':movie.to_dict()}
