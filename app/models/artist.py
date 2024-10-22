from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime,timezone


crew = db.Table(
    'crew',
    db.Model.metadata,
    db.Column('artist_id',db.Integer,db.ForeignKey(add_prefix_for_prod('artists.id')), primary_key=True),
    db.Column('movie_id',db.Integer,db.ForeignKey(add_prefix_for_prod('movies.id')), primary_key=True),
    db.Column('role',db.String(50)),
    db.Column("created_at",db.DateTime, default=lambda: datetime.now(timezone.utc)),
    db.Column("updated_at",db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc)),
    schema=SCHEMA if environment == "production" else None
)

class Artist(db.Model):
    __tablename__ = 'artists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50),nullable=False)
    last_name = db.Column(db.String(50),nullable=False)
    img_url = db.Column(db.String(255), nullable=False)


    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    artist_movies = db.relationship('Movie',secondary=crew,back_populates='movie_artists')


    def to_dict(self):
        return {
            'id':self.id,
            'firstName':self.first_name,
            'lastName':self.last_name,
            'imgUrl':self.img_url,
            'createdAt':self.created_at,
            'updatedAt':self.updated_at
        }
