"""Initial migration.

Revision ID: fed50ce4af2b
Revises: 
Create Date: 2021-11-19 20:07:40.954805

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fed50ce4af2b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('resource_id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.VARCHAR(length=80), nullable=True),
    sa.Column('common_name', sa.VARCHAR(length=80), nullable=True),
    sa.Column('rating', sa.INTEGER(), nullable=True),
    sa.Column('meta_rating', sa.INTEGER(), nullable=False),
    sa.Column('nation', sa.INTEGER(), nullable=True),
    sa.Column('league', sa.INTEGER(), nullable=True),
    sa.Column('club', sa.INTEGER(), nullable=False),
    sa.Column('position', sa.VARCHAR(length=80), nullable=False),
    sa.Column('height', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.INTEGER(), nullable=False),
    sa.Column('attack_work_rate', sa.VARCHAR(length=80), nullable=False),
    sa.Column('defense_work_rate', sa.VARCHAR(length=80), nullable=False),
    sa.Column('foot', sa.VARCHAR(length=80), nullable=False),
    sa.Column('weak_foot', sa.INTEGER(), nullable=False),
    sa.Column('skill_moves', sa.INTEGER(), nullable=False),
    sa.Column('shooting', sa.INTEGER(), nullable=False),
    sa.Column('positioning', sa.INTEGER(), nullable=False),
    sa.Column('finishing', sa.INTEGER(), nullable=False),
    sa.Column('shot_power', sa.INTEGER(), nullable=False),
    sa.Column('long_shots', sa.INTEGER(), nullable=False),
    sa.Column('volleys', sa.INTEGER(), nullable=False),
    sa.Column('penalties', sa.INTEGER(), nullable=False),
    sa.Column('defending', sa.INTEGER(), nullable=False),
    sa.Column('heading_accuracy', sa.INTEGER(), nullable=False),
    sa.Column('interceptions', sa.INTEGER(), nullable=False),
    sa.Column('sliding_tackle', sa.INTEGER(), nullable=False),
    sa.Column('standing_tackle', sa.INTEGER(), nullable=False),
    sa.Column('dribbling_face', sa.INTEGER(), nullable=False),
    sa.Column('agility', sa.INTEGER(), nullable=False),
    sa.Column('balance', sa.INTEGER(), nullable=False),
    sa.Column('ball_control', sa.INTEGER(), nullable=False),
    sa.Column('composure', sa.INTEGER(), nullable=False),
    sa.Column('dribbling', sa.INTEGER(), nullable=False),
    sa.Column('reactions', sa.INTEGER(), nullable=False),
    sa.Column('pace', sa.INTEGER(), nullable=False),
    sa.Column('acceleration', sa.INTEGER(), nullable=False),
    sa.Column('sprint_speed', sa.INTEGER(), nullable=False),
    sa.Column('passing', sa.INTEGER(), nullable=False),
    sa.Column('crossing', sa.INTEGER(), nullable=False),
    sa.Column('curve', sa.INTEGER(), nullable=False),
    sa.Column('free_kick_accuracy', sa.INTEGER(), nullable=False),
    sa.Column('long_passing', sa.INTEGER(), nullable=False),
    sa.Column('short_passing', sa.INTEGER(), nullable=False),
    sa.Column('vision', sa.INTEGER(), nullable=False),
    sa.Column('physicality', sa.INTEGER(), nullable=False),
    sa.Column('aggression', sa.INTEGER(), nullable=False),
    sa.Column('stamina', sa.INTEGER(), nullable=False),
    sa.Column('jumping', sa.INTEGER(), nullable=False),
    sa.Column('strength', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('resource_id')
    )
    # ### end Alembic commands ###