"""adding played to crew

Revision ID: 92e2fc4f0473
Revises: a258846e069f
Create Date: 2024-10-21 21:03:53.479702

"""
from alembic import op
import sqlalchemy as sa


import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

schema = SCHEMA if environment == "production" else None
# revision identifiers, used by Alembic.
revision = '92e2fc4f0473'
down_revision = 'a258846e069f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crew', schema=schema) as batch_op:
        batch_op.add_column(sa.Column('played', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crew', schema=schema) as batch_op:
        batch_op.drop_column('played')

    # ### end Alembic commands ###
