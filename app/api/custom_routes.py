from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import Custom_Movie,db
from datetime import date

custom_routes = Blueprint('customs',__name__)


@custom_routes.route('/')
@login_required
def all_user_customs():
    customs = Custom_Movie.query.filter_by(user_id=current_user.id).all()
    return {'customs':[custom.to_dict() for custom in customs]}



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
