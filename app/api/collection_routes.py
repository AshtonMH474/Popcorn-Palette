from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import db,Collection,Movie
from app.models.collection import collection_movies
from datetime import date


collection_routes = Blueprint('collections',__name__)


@collection_routes.route('/search')
@login_required
def search_collection():

    search_term = request.args.get('query',None)

    if not search_term:
        cols = Collection.query.filter_by(user_id=current_user.id).all()
    else:
        cols = Collection.query.filter(Collection.title.ilike(f'%{search_term}%'),Collection.user_id == current_user.id ).all()

    return {'collections': [col.to_dict() for col in cols]}

@collection_routes.route('/')
@login_required
def get_collections():
    collections = Collection.query.filter_by(user_id=current_user.id).all()
    if len(collections) < 1:
        return {'collections':[]}
    return {'collections': [collection.to_dict() for collection in collections]}



@collection_routes.route('/<int:collection_id>')
@login_required
def get_collection_by_id(collection_id):
    col = Collection.query.filter_by(id=collection_id).first()


    if col is None:
        return {'errors': {'message': 'Collection can not be found'}}, 404
    if col.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401

    return jsonify({'collection': [col.to_dict()]})


@collection_routes.route('/',methods=['POST'])
@login_required
def create_collection():
    data = request.json

    try:
        description = data.get('description')
        title = data.get('title')
        user_id = current_user.id

        new_collection = Collection(user_id=user_id,description=description,title=title)
        db.session.add(new_collection)
        db.session.commit()

        return jsonify({'collection':new_collection.to_dict()}),201

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add Collection"}), 400



@collection_routes.route('/<int:collection_id>',methods=['POST'])
@login_required
def add_to_collection(collection_id):
    data = request.json
    movie = Movie.query.filter_by(id=data.get('id')).first()
    collection = Collection.query.filter_by(id=collection_id).first()


    if movie is None:
        return {'errors': {'message': 'Movie can not be found'}}, 404

    if collection is None:
        return {'errors': {'message': 'Collection can not be found'}}, 404

    if collection.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401

    movie_in_collection=db.session.query(collection_movies).filter_by(collection_id=collection.id,movie_id=movie.id).first()
    if movie_in_collection:
        return {'errors': {'message': 'User has Movie in Collection'}}, 400

    try:
        collection.movies.append(movie)
        db.session.commit()

        return {'movie':movie.to_dict()},201

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add To Collection"}), 400



@collection_routes.route('/<int:collection_id>',methods=['PUT'])
@login_required
def edit_collection(collection_id):
    data = request.json
    collection = Collection.query.filter_by(id=collection_id).first()


    if collection is None:
        return {'errors': {'message': 'Collection can not be found'}}, 404

    if collection.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401


    try:
        collection.title = data.get('title',collection.title)
        collection.description = data.get('description',collection.description)

        db.session.commit()

        return jsonify({'collection':collection.to_dict()})

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Update Collection"}), 400



@collection_routes.route('/<int:collection_id>',methods=['DELETE'])
@login_required
def delete_collection(collection_id):
    collection = Collection.query.filter_by(id=collection_id).first()


    if collection is None:
        return {'errors': {'message': 'Collection can not be found'}}, 404

    if collection.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401

    try:
        db.session.delete(collection)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Collection"}), 400



@collection_routes.route('/<int:collection_id>/movies/<int:movie_id>',methods=['DELETE'])
@login_required
def delete_movie_from_collection(collection_id,movie_id):
    collection = Collection.query.filter_by(id=collection_id).first()
    movie = Movie.query.get(movie_id)


    if movie is None:
        return {'errors': {'message': 'Movie not Found'}}, 404

    if collection is None:
        return {'errors': {'message': 'Collection can not be found'}}, 404

    if collection.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401

    movie_in_collection=db.session.query(collection_movies).filter_by(collection_id=collection.id,movie_id=movie.id).first()

    if movie_in_collection is None:
        return {'errors': {'message': "Movie is not in User's Collection"}}, 404

    try:
        collection.movies.remove(movie)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Movie From Collection"}), 400
