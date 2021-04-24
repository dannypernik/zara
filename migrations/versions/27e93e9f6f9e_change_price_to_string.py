"""change price to string

Revision ID: 27e93e9f6f9e
Revises: b5e254bc4d29
Create Date: 2021-04-23 23:52:22.118062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27e93e9f6f9e'
down_revision = 'b5e254bc4d29'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.NUMERIC(precision=4),
               type_=sa.String(length=5),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('food', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.String(length=5),
               type_=sa.NUMERIC(precision=4),
               existing_nullable=True)

    # ### end Alembic commands ###
