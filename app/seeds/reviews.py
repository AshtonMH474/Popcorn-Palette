from app.models import db, Review,Movie, environment, SCHEMA
from sqlalchemy.sql import text
from .utilis import update_rating


def seed_reviews():
    review1 = Review(
        user_id=1,
        movie_id=11,
        review='Best Transformers Movie I have seen',
        rating=5
    )
    review2 = Review(
        user_id=2,
        movie_id=11,
        review='Wow i am shocked i am saying this but it was perfect. From the first act all the way to the end. It was a fun and impactful movie in the Transformers franchise',
        rating=5
    )
    review3 = Review(
        user_id=3,
        movie_id=11,
        review='Deftintely top 5 transformer movie',
        rating=4
    )

    movie1_reviews = [review1,review2,review3]

    for review in movie1_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(11)

    review4 = Review(
        user_id=1,
        movie_id=66,
        review='Heath Ledger gave one of the best villan performaces I have ever seen.',
        rating=5
    )
    review5 = Review(
        user_id=2,
        movie_id=66,
        review='Christoper Nolan knows what hes doing',
        rating=5
    )
    review6 = Review(
        user_id=3,
        movie_id=66,
        review='Deftintely top 5 movie all time',
        rating=5
    )

    movie2_reviews = [review4,review5,review6]

    for review in movie2_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(66)


    review7 = Review(
        user_id=1,
        movie_id=45,
        review='Amazing performance',
        rating=5
    )
    review8 = Review(
        user_id=2,
        movie_id=45,
        review='Emma Stone was amazing',
        rating=5
    )
    review9 = Review(
        user_id=3,
        movie_id=45,
        review='I get why people love this film',
        rating=4
    )

    movie3_reviews = [review7,review8,review9]

    for review in movie3_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(45)

    review10 = Review(
        user_id=1,
        movie_id=54,
        review='Amazing new addition to the scifi genre',
        rating=5
    )
    review11 = Review(
        user_id=2,
        movie_id=54,
        review='Why do people not wanna see this',
        rating=5
    )
    review12 = Review(
        user_id=3,
        movie_id=54,
        review='I get why people love this film',
        rating=5
    )

    movie4_reviews = [review11,review12,review10]

    for review in movie4_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(54)

    review13 = Review(
        user_id=1,
        movie_id=56,
        review='Would watch again',
        rating=5
    )
    review14 = Review(
        user_id=2,
        movie_id=56,
        review='Top tier',
        rating=5
    )
    review15 = Review(
        user_id=3,
        movie_id=56,
        review='This movie was super well made',
        rating=4
    )

    movie5_reviews = [review13,review14,review15]

    for review in movie5_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(56)


    review16 = Review(
        user_id=1,
        movie_id=64,
        review='The action was insane',
        rating=5
    )
    review17 = Review(
        user_id=2,
        movie_id=64,
        review='Gotta love Kenua Reves',
        rating=5
    )
    review18 = Review(
        user_id=3,
        movie_id=64,
        review='So glad they made another one',
        rating=4
    )

    movie6_reviews = [review16,review17,review18]

    for review in movie6_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(64)

    review19 = Review(
        user_id=1,
        movie_id=57,
        review='This is why I love Movies',
        rating=5
    )
    review20 = Review(
        user_id=2,
        movie_id=57,
        review='The reason I love scifi',
        rating=5
    )
    review21 = Review(
        user_id=3,
        movie_id=57,
        review='Theres a reason this is a classic',
        rating=5
    )

    movie7_reviews = [review19,review20,review21]

    for review in movie7_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(57)

    review22 = Review(
        user_id=1,
        movie_id=61,
        review='Why do I love scifi so much',
        rating=5
    )
    review23 = Review(
        user_id=2,
        movie_id=61,
        review='Im in shock',
        rating=5
    )
    review24 = Review(
        user_id=3,
        movie_id=61,
        review='I get why people love this film',
        rating=5
    )

    movie8_reviews = [review22,review23,review24]

    for review in movie8_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(61)

    review25 = Review(
        user_id=1,
        movie_id=20,
        review='I wanted to leave the theater',
        rating=2
    )
    review26 = Review(
        user_id=2,
        movie_id=20,
        review='Why make this',
        rating=1
    )
    review27 = Review(
        user_id=3,
        movie_id=20,
        review='This is the reason ghostbusters died',
        rating=2
    )

    movie9_reviews = [review25,review26,review27]

    for review in movie9_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(20)


    review28 = Review(
        user_id=1,
        movie_id=68,
        review='This is what we have been waiting on. It all came together perfeclty and shows us whats to come.',
        rating=5
    )
    review29 = Review(
        user_id=2,
        movie_id=68,
        review='The MCU is becoming big i guess',
        rating=4
    )
    review30 = Review(
        user_id=3,
        movie_id=68,
        review='Comedy was there and action and acting abilites',
        rating=4
    )

    movie10_reviews = [review28,review29,review30]

    for review in movie10_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(68)




def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
