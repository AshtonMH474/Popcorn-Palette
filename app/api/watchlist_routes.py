from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import User,Movie,db
from app.models.movie import watchlist
from datetime import date

watchlist_routes = Blueprint('watchlist',__name__)


@watchlist_routes.route('/current')
@login_required
def get_watchlist():
    """
    Query for all movies in watchlist
    """
    user = User.query.filter_by(id=current_user.id).first()

    if user.watchlist_movies is not None and len(user.watchlist_movies) > 0:
        movies = []

        for movie in user.watchlist_movies:
            movie_in_watchlist=db.session.query(watchlist).filter_by(user_id=current_user.id,movie_id=movie.id).first()
            watched = movie_in_watchlist.watched

            movie_data=movie.to_dict()
            movie_data['watched'] = watched
            movies.append(movie_data)

        return {'watchlistMovies': movies}
    else:
        return {'watchlistMovies':[]}



@watchlist_routes.route('/',methods=['POST'])
@login_required
def add_to_watchlist():
    user = User.query.filter_by(id=current_user.id).first()
    data = request.json


    movie_id = data.get('movieId')
    movie=Movie.query.filter_by(id=movie_id).first()

    if movie is None:
        return {'errors': {'message': 'Movie can not be found'}}, 404


    user_watchlist_movie=db.session.query(watchlist).filter_by(user_id=current_user.id,movie_id=movie.id).first()
    if user_watchlist_movie:
            return {'errors': {'message': 'User has Movie in watchlist'}}, 400

    try:
        user.watchlist_movies.append(movie)
        db.session.commit()

        return {'movie': movie.to_dict()},201

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add To Watchlist"}), 400



@watchlist_routes.route('/<int:movie_id>',methods=['PUT'])
@login_required
def watched_movie(movie_id):
    movie=Movie.query.filter_by(id=movie_id).first()

    if movie is None:
        return {'errors': {'message': 'Movie Not Found'}}, 404

    movie_in_watchlist=db.session.query(watchlist).filter_by(user_id=current_user.id,movie_id=movie.id).first()

    if movie_in_watchlist is None:
        return {'errors': {'message': 'User does not have Movie in watchlist'}}, 404

    if movie_in_watchlist.watched is False:
        db.session.execute(
            watchlist.update().where(
                (watchlist.c.user_id == current_user.id) &
                (watchlist.c.movie_id == movie_id)
            ).values(watched=True)
        )
    else:
        db.session.execute(
            watchlist.update().where(
                (watchlist.c.user_id == current_user.id) &
                (watchlist.c.movie_id == movie_id)
            ).values(watched=False)
        )
    db.session.commit()

    movie_in_watchlist=db.session.query(watchlist).filter_by(user_id=current_user.id,movie_id=movie.id).first()
    watched=movie_in_watchlist.watched

    movie_data = movie.to_dict()
    movie_data['watched'] = watched

    return {'movie':movie_data}



@watchlist_routes.route('/<int:movie_id>',methods=['DELETE'])
@login_required
def delete_from_inventory(movie_id):
    movie=Movie.query.get(movie_id)
    if movie is None:
        return {'errors': {'message': 'Movie not Found'}}, 404

    movie_in_watchlist=db.session.query(watchlist).filter_by(user_id=current_user.id,movie_id=movie.id).first()
    if movie_in_watchlist is None:
        return {'errors': {'message': "Movie is not in User's Watchlist"}}, 404

    user = User.query.filter_by(id=current_user.id).first()
    try:
        user.watchlist_movies.remove(movie)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't delete from Watchlist"}), 400
