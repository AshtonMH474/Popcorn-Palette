from app.models import db, Custom_Movie,Genre,Custom_Image,environment, SCHEMA
from sqlalchemy.sql import text
from datetime import date



def seed_custom():
    randomMovie1 = Custom_Movie(
    title="Lego Car",
    user_id=1,
    description="The battle between friends and foes in the ultimate lego car race",
    release_date=date(2023, 10, 6)
    )

    randomMovie2 = Custom_Movie(
    title="Space Cowboys: The Galactic Rodeo",
    user_id=1,
    description="A group of cowboy outlaws travel through space, riding asteroid beasts and escaping galactic law enforcement in an interstellar rodeo competition.",
    release_date=date(2023, 11, 1)
)

    randomMovie3 = Custom_Movie(
    title="Zombie Pizza Delivery",
    user_id=1,
    description="In a post-apocalyptic world, a group of survivors is determined to keep their pizza business running while delivering orders to the most dangerous zombie-infested areas.",
    release_date=date(2024, 1, 15)
)

    custom_movies = [randomMovie1,randomMovie2,randomMovie3]

    for custom in custom_movies:
        db.session.add(custom)

    db.session.commit()

    action = Genre.query.filter_by(type='Action').first()
    adventure = Genre.query.filter_by(type='Adventure').first()
    drama = Genre.query.filter_by(type='Drama').first()
    horror = Genre.query.filter_by(type='Horror').first()
    sci = Genre.query.filter_by(type='Science Fiction').first()


    randomMovie1.genres.append(action)
    randomMovie1.genres.append(drama)
    randomMovie1.genres.append(adventure)

    randomMovie2.genres.append(sci)
    randomMovie2.genres.append(horror)
    randomMovie2.genres.append(adventure)

    randomMovie3.genres.append(horror)
    randomMovie3.genres.append(action)
    randomMovie3.genres.append(adventure)

    db.session.commit()


    image1 = Custom_Image(custom_id=1,img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1731451206/s-l1200_g01bfd.jpg')
    image2 = Custom_Image(custom_id=2,img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1731451206/7861c6c9d8f98b6c94d88d2c16518bdb_cykk9l.jpg')
    image3 = Custom_Image(custom_id=3,img_url='https://res.cloudinary.com/dzsguqdmg/image/upload/v1731451206/de0hrb3-a0c81d7a-6f07-470d-8265-788132ecda68_rf4ary.jpg')

    images = [image1,image2,image3]

    for image in images:
        db.session.add(image)
    db.session.commit()




def undo_custom():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.custom_movies RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.custom_movie_genres RESTART IDENTITY CASCADE;")
        db.session.execute(f"TRUNCATE table {SCHEMA}.custom_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM custom_movies"))
        db.session.execute(text("DELETE FROM custom_movie_genres"))
        db.session.execute(text("DELETE FROM custom_images"))

    db.session.commit()
