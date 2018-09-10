"""Add customer foreign key

Revision ID: ccd5b0142a76
Revises: 243adac5e3e9
Create Date: 2017-03-14 18:59:50.505319

"""

# revision identifiers, used by Alembic.
revision = 'ccd5b0142a76'
down_revision = '243adac5e3e9'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('hail_customer_id', 'hail', 'customer', ['customer_id', 'added_by'], ['id', 'moteur_id'])
    ### end Alembic commands ###


def downgrade():
    op.drop_constraint('hail_customer_id', 'hail', type_='foreignkey')
