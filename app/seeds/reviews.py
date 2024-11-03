from app.models import db, Review,Movie, environment, SCHEMA
from sqlalchemy.sql import text
from .utilis import update_rating


def seed_reviews():
    review1 = Review(
        user_id=1,
        movie_id=698687,
        review='Best Transformers Movie I have seen',
        rating=5
    )
    review2 = Review(
        user_id=2,
        movie_id=698687,
        review='Wow i am shocked i am saying this but it was perfect. From the first act all the way to the end. It was a fun and impactful movie in the Transformers franchise',
        rating=5
    )
    review3 = Review(
        user_id=3,
        movie_id=698687,
        review='Deftintely top 5 transformer movie',
        rating=4
    )

    movie1_reviews = [review1,review2,review3]

    for review in movie1_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(698687)

    review4 = Review(
        user_id=1,
        movie_id=155,
        review='Heath Ledger gave one of the best villan performaces I have ever seen.',
        rating=5
    )
    review5 = Review(
        user_id=2,
        movie_id=155,
        review='Christoper Nolan knows what hes doing',
        rating=5
    )
    review6 = Review(
        user_id=3,
        movie_id=155,
        review='Deftintely top 5 movie all time',
        rating=5
    )

    movie2_reviews = [review4,review5,review6]

    for review in movie2_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(155)


    # review7 = Review(
    #     user_id=1,
    #     movie_id=533535,
    #     review='Deadpool was not ruined',
    #     rating=4
    # )
    # review8 = Review(
    #     user_id=2,
    #     movie_id=45,
    #     review='Hugh Jackman was amazing',
    #     rating=5
    # )
    # review9 = Review(
    #     user_id=3,
    #     movie_id=533535,
    #     review='I get why people love this film',
    #     rating=4
    # )

    # movie3_reviews = [review7,review8,review9]

    # for review in movie3_reviews:
    #     db.session.add(review)
    # db.session.commit()

    # update_rating(533535)

    review10 = Review(
        user_id=1,
        movie_id=1022789,
        review='Love this',
        rating=5
    )
    review11 = Review(
        user_id=2,
        movie_id=1022789,
        review='Pixar gets it',
        rating=5
    )
    review12 = Review(
        user_id=3,
        movie_id=1022789,
        review='I get why people love this film',
        rating=5
    )

    movie4_reviews = [review11,review12,review10]

    for review in movie4_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(1022789)

    review13 = Review(
        user_id=1,
        movie_id=912649,
        review='It was om',
        rating=3
    )
    review14 = Review(
        user_id=2,
        movie_id=912649,
        review='Good way to end triolgy',
        rating=4
    )
    review15 = Review(
        user_id=3,
        movie_id=912649,
        review='It was good but prob will never watch again',
        rating=3
    )

    movie5_reviews = [review13,review14,review15]

    for review in movie5_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(912649)


    review16 = Review(
        user_id=1,
        movie_id=603692,
        review='The action was insane',
        rating=5
    )
    review17 = Review(
        user_id=2,
        movie_id=603692,
        review='Gotta love Kenua Reves',
        rating=5
    )
    review18 = Review(
        user_id=3,
        movie_id=603692,
        review='So glad they made another one',
        rating=4
    )

    movie6_reviews = [review16,review17,review18]

    for review in movie6_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(603692)

    review19 = Review(
        user_id=1,
        movie_id=11,
        review='This is why I love Movies',
        rating=5
    )
    review20 = Review(
        user_id=2,
        movie_id=11,
        review='The reason I love scifi',
        rating=5
    )
    review21 = Review(
        user_id=3,
        movie_id=11,
        review='Theres a reason this is a classic',
        rating=5
    )

    movie7_reviews = [review19,review20,review21]

    for review in movie7_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(11)

    review22 = Review(
        user_id=1,
        movie_id=945961,
        review='Alien fans will like this',
        rating=4
    )
    review23 = Review(
        user_id=2,
        movie_id=945961,
        review='Im in shock',
        rating=4
    )
    review24 = Review(
        user_id=3,
        movie_id=945961,
        review='Way better then expected',
        rating=4
    )

    movie8_reviews = [review22,review23,review24]

    for review in movie8_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(945961)

    review25 = Review(
        user_id=1,
        movie_id=385687,
        review='this was crazy',
        rating=4
    )
    review26 = Review(
        user_id=2,
        movie_id=385687,
        review='It was fun but not great',
        rating=3
    )
    review27 = Review(
        user_id=3,
        movie_id=385687,
        review='This needs to end',
        rating=2
    )

    movie9_reviews = [review25,review26,review27]

    for review in movie9_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(385687)


    review28 = Review(
        user_id=1,
        movie_id=9479,
        review='Classic',
        rating=5
    )
    review29 = Review(
        user_id=2,
        movie_id=9479,
        review='Woahhh love this',
        rating=5
    )
    review30 = Review(
        user_id=3,
        movie_id=9479,
        review='Always come back to this',
        rating=5
    )

    movie10_reviews = [review28,review29,review30]

    for review in movie10_reviews:
        db.session.add(review)
    db.session.commit()

    update_rating(9479)




def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM reviews"))

    db.session.commit()
