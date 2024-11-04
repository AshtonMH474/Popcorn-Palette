from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime,timezone

collection_movies = db.Table(
    'collection_movies',
    db.Model.metadata,
    db.Column('movie_id',db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')), primary_key=True),
    db.Column('collection_id',db.Integer,db.ForeignKey(add_prefix_for_prod('collections.id')), primary_key=True),
    db.Column("created_at",db.DateTime, default=lambda: datetime.now(timezone.utc)),
    db.Column("updated_at",db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)),
    schema=SCHEMA if environment == "production" else None
)


class Collection(db.Model):
    __tablename__ = 'collections'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text,nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')),nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    user = db.relationship('User', back_populates='collections')
    movies = db.relationship('Movie',secondary=collection_movies,back_populates='collections')

    def to_dict(self):
        new_dict = {
        'id':self.id,
        'title':self.title,
        'description':self.description,
        'userId':self.user_id,
        'createdAt':self.created_at,
        'updatedAt':self.updated_at
        }

        if self.movies:
            new_dict['movies'] = [movie.to_dict() for movie in self.movies]

        return new_dict
