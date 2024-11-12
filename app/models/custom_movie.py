from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone

custom_movie_genres = db.Table(
    'custom_movie_genres',
    db.Model.metadata,
    db.Column('custom_movie_id',db.Integer,db.ForeignKey(add_prefix_for_prod('custom_movies.id')), primary_key=True),
    db.Column('genre_id',db.Integer,db.ForeignKey(add_prefix_for_prod('genres.id')), primary_key=True),
    db.Column("created_at",db.DateTime, default=lambda: datetime.now(timezone.utc)),
    db.Column("updated_at",db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)),
    schema=SCHEMA if environment == "production" else None
)

class Custom_Movie(db.Model):
    __tablename__ = 'custom_movies'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')),nullable=False)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=True)
    release_date = db.Column(db.Date,nullable=False)
    avg_rating = db.Column(db.Float,nullable=False,default=0.0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


    user = db.relationship('User',back_populates='movies')

    genres = db.relationship('Genre',secondary=custom_movie_genres,back_populates='custom')


    movie_images=db.relationship('Custom_Image', back_populates='movie', cascade='all, delete-orphan')


    def to_dict(self):
        new_dict =  {
            'id':self.id,
            'userId':self.user_id,
            'title':self.title,
            'description':self.description,
            'releaseDate':self.release_date,
            'avgRating':self.avg_rating,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }

        if self.movie_images:
            new_dict['movieImages'] = [image.to_dict() for image in self.movie_images]
        if self.genres and len(self.genres) > 0:
            new_dict['genres'] = [genre.to_dict() for genre in self.genres]

        return new_dict
