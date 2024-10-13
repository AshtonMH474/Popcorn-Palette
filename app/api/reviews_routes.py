from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import Review,Movie,db

review_routes = Blueprint('reviews',__name__)


@review_routes.route('/current')
@login_required
def get_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return {'reviews':[review.to_dict() for review in reviews]}



@review_routes.route('/',methods=['POST'])
@login_required
def make_review():
    data = request.json


    movie_id = data.get('movieId')
    movie=Movie.query.filter_by(id=movie_id).first()



    if movie is None:
        return {'errors': {'message': 'Movie can not be found'}}, 404

    current_review = Review.query.filter_by(movie_id=movie_id,user_id=current_user.id)
    if current_review is not None:
        return {'errors': {'message':'User already has a review for this movie'}}

    try:
        review = data.get('review')
        rating = data.get('rating')

        the_review = Review(
            user_id=current_user.id,
            movie_id=movie_id,
            review=review,
            rating=rating
        )
        db.session.add(the_review)
        db.session.commit()

        return jsonify({'review':review.to_dict()}),201
    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Add Review"}), 400



@review_routes.route('/<int:review_id>',methods=['PUT'])
@login_required
def update_review(review_id):
    data=request.json

    review = Review.query.get(review_id)

    if review is None:
        return {'errors':{'message':'Review not Found'}},404

    if review.user_id != current_user.id:
        return {'errors': {'message': 'Unauthorized'}}, 401

    try:
        review.review=data.get('review',review.review)
        review.rating=data.get('rating',review.rating)

        db.session.commit()


        return jsonify({'review':review.to_dict()})

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Update Review"}), 400


@review_routes.route('/<int:review_id>',methods=['DELETE'])
@login_required
def delete_review(review_id):
    review = Review.query.get(review_id)

    if review is None:
        return {'errors':{'message':'Review not Found'}},404

    if review.user_id != current_user.id:
        return {'errors': {'message': 'Unauthorized'}}, 401

    try:
        db.session.delete(review)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Review"}), 400
