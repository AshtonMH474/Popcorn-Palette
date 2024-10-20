"""genres

Revision ID: ee94f7f268fb
Revises: 0209ec006de6
Create Date: 2024-10-19 19:19:35.288060

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = 'ee94f7f268fb'
down_revision = '0209ec006de6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_genres',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'genre_id')
    )
    # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE genres SET SCHEMA {SCHEMA};")
    if environment == "production":
        op.execute(f"ALTER TABLE movie_genres SET SCHEMA {SCHEMA};")

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_genres')
    op.drop_table('genres')
    # ### end Alembic commands ###