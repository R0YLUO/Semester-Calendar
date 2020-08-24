"""empty message

Revision ID: 9bae26b5408b
Revises: 4fcda75856d5
Create Date: 2020-08-24 16:49:37.522898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bae26b5408b'
down_revision = '4fcda75856d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('has_calendar', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('has_calendar')

    # ### end Alembic commands ###
