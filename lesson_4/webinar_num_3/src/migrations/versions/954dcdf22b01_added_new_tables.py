"""ADDED NEW TABLES

Revision ID: 954dcdf22b01
Revises: 2c5b35619743
Create Date: 2022-07-20 13:09:53.828979

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '954dcdf22b01'
down_revision = '2c5b35619743'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('title', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('created_at', str(sa.DateTime()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('uuid', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('roles', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('created_at', str(sa.DateTime()), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_totp_enabled', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password_hash', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('posts')
    # ### end Alembic commands ###
