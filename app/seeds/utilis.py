from app.models import db, Review,Movie

def update_rating(movie_id):
    all_reviews = Review.query.filter_by(movie_id=movie_id).all()
    average = get_average(all_reviews)
    movie = Movie.query.filter_by(id=movie_id).first()

    movie.avg_rating = average

    db.session.commit()



def get_average(reviews):
    num = 0
    for review in   reviews:
        num = num + review.rating
    average = num / len(reviews)
    return average



def get_all_review_movie_ids():
    all_reviews = Review.query.with_entities(Review.movie_id).all()
    new_set = set()

    for review in all_reviews:
        new_set.add(review.movie_id)

    return list(new_set)
