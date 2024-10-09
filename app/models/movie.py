from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone

watchlist = db.Table(
    'watchlist',
    db.Model.metadata,
    db.Column('user_id',db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('movie_id',db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')), primary_key=True),
    db.Column('watched',db.Boolean,default=False),
    db.Column('watched_date',db.Date,nullable=True),
    db.Column("created_at",db.DateTime, default=lambda: datetime.now(timezone.utc)),
    db.Column("updated_at",db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)),
    schema=SCHEMA if environment == "production" else None
)

class Movie(db.Model):
    __tablename__ = 'movies'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')),nullable=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=True)
    release_date = db.Column(db.Date,nullable=False)
    avg_rating = db.Column(db.Float,nullable=False,default=0.0)
    custom = db.Column(db.Boolean, nullable=False,default=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    movie_images=db.relationship('Movie_Image', back_populates='movie', cascade='all, delete-orphan')
    user = db.relationship('User', back_populates='movies')

    users_watchlist=db.relationship('User',secondary=watchlist,back_populates='watchlist_movies')


    def to_dict(self):
        new_dict =  {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'releaseDate':self.release_date,
            'avgRating':self.avg_rating,
            'custom':self.custom,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }
        if self.user_id:
            new_dict['userId']=self.user_id
        if self.movie_images:
            new_dict['movieImages'] = [image.to_dict() for image in self.movie_images]

        return new_dict
