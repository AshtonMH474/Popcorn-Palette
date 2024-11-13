import os
import cloudinary


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here (for production)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = True


    CLOUD_NAME = 'dzsguqdmg'
    API_KEY = 567866934876169
    API_SECRET = 'SWPcBeI8FqxZ9Fv4I0tVHB1D9Rk'


    def init_cloudinary():
        cloudinary.config(
            cloud_name=Config.CLOUD_NAME,
            api_key=Config.API_KEY,
            api_secret=Config.API_SECRET
        )
