from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime,timezone

movie_genres = db.Table(
    'movie_genres',
    db.Model.metadata,
    db.Column('movie_id',db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')), primary_key=True),
    db.Column('genre_id',db.Integer,db.ForeignKey(add_prefix_for_prod('genres.id')), primary_key=True),
    db.Column("created_at",db.DateTime, default=lambda: datetime.now(timezone.utc)),
    db.Column("updated_at",db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)),
    schema=SCHEMA if environment == "production" else None
)

class Genre(db.Model):
    __tablename__ = 'genres'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # movies
    movies = db.relationship('Movie',secondary=movie_genres,back_populates='genres')

    def to_dict(self):
        new_dict = {
            'id':self.id,
            'type':self.type,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }

        return new_dict
