"""empty message

Revision ID: a82bdbc4b734
Revises: 75e7038ed13b
Create Date: 2020-08-22 17:23:02.788046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a82bdbc4b734'
down_revision = '75e7038ed13b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('week', schema=None) as batch_op:
        batch_op.create_foreign_key(batch_op.f('fk_week_calendar_id_calendar'), 'calendar', ['calendar_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('week', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_week_calendar_id_calendar'), type_='foreignkey')

    # ### end Alembic commands ###