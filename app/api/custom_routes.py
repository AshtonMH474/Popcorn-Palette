from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import Custom_Movie,Custom_Image,db,Genre
from app.models.custom_movie import custom_movie_genres
from datetime import date
import cloudinary.uploader
import cloudinary.api

custom_routes = Blueprint('customs',__name__)


@custom_routes.route('/genres/search')
@login_required
def search_genres():
    search_term = request.args.get('query',None)

    if not search_term:
        genres = Genre.query.all()

    else:
        genres = Genre.query.filter(Genre.type.ilike(f'%{search_term}%')).all()

    return {'genres': [genre.to_dict() for genre in genres]}

@custom_routes.route('/')
@login_required
def all_user_customs():
    customs = Custom_Movie.query.filter_by(user_id=current_user.id).all()
    return {'customs':[custom.to_dict() for custom in customs]}


@custom_routes.route('/<int:custom_id>')
@login_required
def custom_details(custom_id):
    custom= Custom_Movie.query.filter_by(id=custom_id).first()

    if custom is None:
        return {'errors':{'message':'Custom not Found'}},404

    if custom.user_id != current_user.id:
        return {'errors': {'message': 'Unauthorized'}}, 401

    return jsonify({'custom':custom.to_dict()})



@custom_routes.route('/',methods=['POST'])
@login_required
def create_custom():
    data = request.json


    try:
        title = data.get('title')
        description = data.get('description')
        release_date_list = data.get('releaseDate').split('-')

        if release_date_list is None:
            return jsonify({'error': "No release Date"}), 400

        if len(release_date_list) < 3:
            return jsonify({'error': "Release Date in wrong format"}), 400

        custom = Custom_Movie(user_id=current_user.id,title=title,description=description,release_date=date(int(release_date_list[0]),int(release_date_list[1]),int(release_date_list[2])))


        db.session.add(custom)
        db.session.commit()

        return jsonify({'custom':custom.to_dict()}),201

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add Custom"}), 400



@custom_routes.route('/<int:custom_id>',methods=['PUT'])
@login_required
def update_custom(custom_id):
    data=request.json

    custom = Custom_Movie.query.get(custom_id)

    if custom is None:
        return {'errors':{'message':'Custom not Found'}},404

    if custom.user_id != current_user.id:
        return {'errors': {'message': 'Unauthorized'}}, 401

    try:
        custom.title= data.get('title',custom.title)
        custom.description= data.get('description',custom.description)
        release_date = data.get('releaseDate',custom.release_date)

        if release_date is not custom.release_date:
            release_date_list = release_date.split('-')
            if release_date_list is None or len(release_date_list) < 3:
                custom.release_date = custom.release_date
            else:
                custom.release_date = date(int(release_date_list[0]),int(release_date_list[1]),int(release_date_list[2]))

        db.session.commit()

        return jsonify({'custom':custom.to_dict()})

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Update Custom"}), 400




@custom_routes.route('/<int:custom_id>',methods=['DELETE'])
@login_required
def delete_custom(custom_id):
    custom = Custom_Movie.query.get(custom_id)

    if custom is None:
        return {'errors':{'message':'Custom not Found'}},404

    if custom.user_id != current_user.id:
        return {'errors': {'message': 'Unauthorized'}}, 401

    try:
        db.session.delete(custom)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Custom"}), 400


@custom_routes.route('/<int:custom_id>/genres/<int:genre_id>',methods=["POST"])
@login_required
def add_genre_custom_movie(custom_id,genre_id):
    custom = Custom_Movie.query.filter_by(id=custom_id).first()
    genre = Genre.query.filter_by(id=genre_id).first()

    if custom is None:
        return {'errors': {'message': 'Custom can not be found'}}, 404
    if genre is None:
        return {'errors': {'message': 'Genre can not be found'}}, 404
    if custom.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401


    genre_in_custom=db.session.query(custom_movie_genres).filter_by(custom_movie_id=custom.id,genre_id=genre.id).first()

    if genre_in_custom is not None:
        return {'errors': {'message': "Genre is in User's Custom"}}, 400

    try:
        custom.genres.append(genre)
        db.session.commit()

        return jsonify({'custom':custom.to_dict()})

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add Genre To Custom"}), 400



@custom_routes.route('/<int:custom_id>/genres/<int:genre_id>',methods=["DELETE"])
@login_required
def delete_genre_from_movie(custom_id,genre_id):
    custom = Custom_Movie.query.filter_by(id=custom_id).first()
    genre = Genre.query.filter_by(id=genre_id).first()


    if custom is None:
        return {'errors': {'message': 'Custom can not be found'}}, 404
    if genre is None:
        return {'errors': {'message': 'Genre can not be found'}}, 404


    genre_in_custom=db.session.query(custom_movie_genres).filter_by(custom_movie_id=custom.id,genre_id=genre.id).first()

    if genre_in_custom is None:
        return {'errors': {'message': "Genre is not in User's Custom"}}, 400

    try:
        custom.genres.remove(genre)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Genre From Custom"}), 400



@custom_routes.route('/<int:custom_id>/images',methods=["POST"])
@login_required
def add_image(custom_id):
    custom = Custom_Movie.query.filter_by(id=custom_id).first()

    if custom is None:
        return {'errors': {'message': 'Custom can not be found'}}, 404

    if custom.user_id != current_user.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401

    data=request.json

    img_url = data.get('imgUrl')
    if img_url is None:
        return {'errors': {'message': 'No Image'}}, 400

    try:
        upload_result = cloudinary.uploader.upload(img_url)
        uploaded_image_url = upload_result['secure_url']


        new_image = Custom_Image(
            custom_id=custom.id,  # Link image to the custom object
            img_url=uploaded_image_url,  # Store the Cloudinary image URL
        )

        db.session.add(new_image)
        db.session.commit()

        return jsonify({'custom':custom.to_dict()})

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add Image To Custom"}), 400




@custom_routes.route('/<int:custom_id>/images/<int:image_id>',methods=["DELETE"])
@login_required
def remove_image(custom_id,image_id):
    custom = Custom_Movie.query.filter_by(id=custom_id).first()
    img = Custom_Image.query.filter_by(id=image_id).first()

    if custom is None:
        return {'errors': {'message': 'Custom can not be found'}}, 404

    if img is None:
        return {'errors': {'message': 'Image can not be found'}}, 404


    if custom.user_id != current_user.id or img.custom_id != custom.id:
        return {'errors': {'message': 'Not Authoarzied'}}, 401


    try:
        db.session.delete(img)
        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Image From Custom"}), 400
