"""empty message

Revision ID: 4411924777df
Revises: 
Create Date: 2021-05-24 17:43:12.882701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4411924777df'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('client_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.Column('postal_code', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('videos_checked_out_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_table('videos',
    sa.Column('video_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('total_inventory', sa.Integer(), nullable=True),
    sa.Column('available_inventory', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('video_id')
    )
    op.create_table('rentals',
    sa.Column('rental_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('vhs_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('due_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.client_id'], ),
    sa.ForeignKeyConstraint(['vhs_id'], ['videos.video_id'], ),
    sa.PrimaryKeyConstraint('rental_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rentals')
    op.drop_table('videos')
    op.drop_table('customers')
    # ### end Alembic commands ###
