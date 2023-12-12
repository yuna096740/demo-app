"""create_post_table

Revision ID: 14eae52b4e31
Revises: 
Create Date: 2023-12-12 01:32:57.216828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14eae52b4e31'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'post',
        sa.Column('id', sa.BigInteger(), autoincrement=True, primary_key=True, nullable=False),
        sa.Column('title', sa.String(80), nullable=False),
        sa.Column('detail', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('post')
