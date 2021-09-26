"""add a category

Revision ID: 9e4a13f37453
Revises: f76eb57b7668
Create Date: 2021-09-26 23:56:03.028095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e4a13f37453'
down_revision = 'f76eb57b7668'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('category', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_blogs_category'), 'blogs', ['category'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blogs_category'), table_name='blogs')
    op.drop_column('blogs', 'category')
    # ### end Alembic commands ###
