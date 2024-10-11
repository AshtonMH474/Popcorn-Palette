from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone


class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')),nullable=False)
    movie_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')),nullable=False)
    review = db.Column(db.Text,nullable=False)
    rating = db.Column(db.Float,nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = db.relationship('User',back_populates='reviews')
    movie = db.relationship('Movie',back_populates='reviews')


    def to_dict(self):
        return {
            'id':self.id,
            'userId':self.user_id,
            'movieId':self.movie_id,
            'review':self.review,
            'rating':self.rating,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }
