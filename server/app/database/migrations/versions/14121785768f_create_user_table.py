"""create_user_table

Revision ID: 14121785768f
Revises: 14eae52b4e31
Create Date: 2023-12-14 23:30:08.944175

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14121785768f'
down_revision: Union[str, None] = '14eae52b4e31'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
