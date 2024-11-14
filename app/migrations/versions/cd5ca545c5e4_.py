"""empty message

Revision ID: cd5ca545c5e4
Revises: 34d8f31376d6
Create Date: 2024-11-12 15:12:30.601149

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd5ca545c5e4'
down_revision: Union[str, None] = '34d8f31376d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
