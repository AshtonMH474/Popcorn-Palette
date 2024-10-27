from flask import Blueprint, jsonify,request
from flask_login import login_required,current_user
from app.models import Review,Movie,db
# from app.seeds.utilis import update_rating, get_average,get_all_review_movie_ids
from app.seeds.utilis import get_average,get_all_review_movie_ids,update_rating
from datetime import date

review_routes = Blueprint('reviews',__name__)

@review_routes.route('/highly_rated')
def get_highly_rated():
    movie_ids  = get_all_review_movie_ids()
    new_list = []
    for movie_id in movie_ids:
        all_reviews = Review.query.filter_by(movie_id=movie_id).all()
        average = get_average(all_reviews)
        if average  > 4.5:
            new_list.append(movie_id)

    return {'movie_ids':new_list}




@review_routes.route('/current')
@login_required
def get_reviews():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return {'reviews':[review.to_dict() for review in reviews]}


@review_routes.route('/<int:movie_id>')
def get_movie_reviews(movie_id):
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    return {'reviews':[review.to_dict() for review in reviews]}

@review_routes.route('/',methods=['POST'])
@login_required
def make_review():
    data = request.json


    movie_id = data.get('movieId')
    movie=Movie.query.filter_by(id=movie_id).first()



    if movie is None:
        # return {'errors': {'message': 'Movie can not be found'}}, 404
        release_date_arr= data.get('releaseDate').split('-')
        title = data.get('title')
        id = data.get('id')

        movie = Movie(id=id,title=title,release_date=date(int(release_date_arr[0]),int(release_date_arr[1]),int(release_date_arr[2])),custom=False)
        db.session.add(movie)

    current_review = Review.query.filter_by(movie_id=movie_id,user_id=current_user.id).first()
    if current_review and getattr(current_review,'id',None) is not None:
        return {'errors': {'message':'User already has a review for this movie'}},400

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

        update_rating(movie_id)

        return jsonify({'review':the_review.to_dict()}),201
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

    movie=Movie.query.filter_by(id=review.movie_id).first()

    try:
        review.review=data.get('review',review.review)
        review.rating=data.get('rating',review.rating)

        db.session.commit()

        update_rating(movie.id)
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

    movie=Movie.query.filter_by(id=review.movie_id).first()

    try:
        db.session.delete(review)
        db.session.commit()

        if len(movie.reviews) == 0:
            movie.avg_rating = 0
        else:
            update_rating(movie.id)

        db.session.commit()

        return {"message":"Successfully deleted"},200

    except Exception:
        db.session.rollback()
        return jsonify({'error': "Couldn't Delete Review"}), 400


@review_routes.route('/avgRating/<int:movie_id>')
def avgRating(movie_id):
    reviews = Review.query.filter_by(movie_id=movie_id).all()

    if len(reviews) == 0:
        return jsonify({
        'avgRating': 0, 'numReviews':0
    })

    count = 0
    for review in reviews:
        count += review.rating
    avergae = count / len(reviews)

    return jsonify({
        'avgRating': avergae, 'numReviews':len(reviews)
    })
