from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone

class Movie_Image(db.Model):
    __tablename__ = 'movie_images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')),nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    public_id = db.Column(db.String(255), nullable=True)
    poster = db.Column(db.Boolean,nullable=False,default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    movie = db.relationship('Movie',back_populates='movie_images')


    def to_dict(self):
        new_dict = {
            'id':self.id,
            'movieId':self.movie_id,
            'imgUrl':self.img_url,
            'poster':self.poster,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }

        if self.public_id:
            new_dict['publicId']=self.public_id

        return new_dict
