"""empty message

Revision ID: f181d8a11a39
Revises: 7ae22050043d
Create Date: 2019-06-26 22:41:27.716859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f181d8a11a39'
down_revision = '7ae22050043d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog_post', 'today',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('blog_post', 'today',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###
