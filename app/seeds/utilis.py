from app.models import db, Review,Movie

def update_rating(movie_id):
    all_reviews = Review.query.filter_by(movie_id=movie_id).all()
    num = 0
    for review in   all_reviews:
        num = num + review.rating
    average = num / len(all_reviews)
    movie = Movie.query.filter_by(id=movie_id).first()

    movie.avg_rating = average

    db.session.commit()
