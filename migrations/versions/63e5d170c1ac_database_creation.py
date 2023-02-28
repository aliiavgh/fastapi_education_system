"""Database creation

Revision ID: 63e5d170c1ac
Revises: 
Create Date: 2023-02-28 20:11:18.237733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63e5d170c1ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('experience', sa.Enum('лично, частным образои', 'лично, профессионально', 'онлайн', 'другое', name='experience_user_enum'), nullable=True),
        sa.Column('audience', sa.Enum('лично, частным образои', 'лично, профессионально', 'онлайн', 'другое', name='experience_user_enum'), nullable=True),
        sa.Column('type', sa.Enum('admin', 'mentor', 'student', name='type_user_enum'), nullable=True),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('is_superuser', sa.Boolean(), nullable=False),
        sa.Column('is_mentor', sa.Boolean(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=True),
        sa.Column('last_name', sa.String(length=50), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profile',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('competence', sa.Integer(), nullable=True),
        sa.Column('language', sa.String(length=50), nullable=True),
        sa.Column('site_url', sa.String(length=180), nullable=True),
        sa.Column('twitter_url', sa.String(length=180), nullable=True),
        sa.Column('facebook_url', sa.String(length=180), nullable=True),
        sa.Column('linkedin_url', sa.String(length=180), nullable=True),
        sa.Column('image', sa.Text(), nullable=True),
        sa.Column('is_hidden', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profile_user_id'), 'profile', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_profile_user_id'), table_name='profile')
    op.drop_table('profile')
    op.drop_table('user')
    # ### end Alembic commands ###
