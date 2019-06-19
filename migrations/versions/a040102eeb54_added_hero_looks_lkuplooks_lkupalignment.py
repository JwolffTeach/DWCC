"""Added Hero_Looks, LKUPLooks, LKUPAlignment

Revision ID: a040102eeb54
Revises: ffe8bfa850f1
Create Date: 2019-06-19 05:21:43.813048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a040102eeb54'
down_revision = 'ffe8bfa850f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lkup_alignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=4096), nullable=True),
    sa.Column('alignment_name', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lkup_looks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=4096), nullable=True),
    sa.Column('look_type', sa.String(length=4096), nullable=True),
    sa.Column('look_details', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero__looks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=True),
    sa.Column('eyes', sa.String(length=4096), nullable=True),
    sa.Column('hair', sa.String(length=4096), nullable=True),
    sa.Column('clothing', sa.String(length=4096), nullable=True),
    sa.Column('body', sa.String(length=4096), nullable=True),
    sa.Column('skin', sa.String(length=4096), nullable=True),
    sa.Column('symbol', sa.String(length=4096), nullable=True),
    sa.ForeignKeyConstraint(['hero_id'], ['hero.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero__looks')
    op.drop_table('lkup_looks')
    op.drop_table('lkup_alignment')
    # ### end Alembic commands ###