"""init todos table

Revision ID: bbe087e02d36
Revises: 
Create Date: 2025-04-28 07:09:59.978428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bbe087e02d36'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_request_logs_id', table_name='request_logs')
    op.drop_table('request_logs')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request_logs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('method', sa.VARCHAR(), nullable=False),
    sa.Column('url', sa.VARCHAR(), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_request_logs_id', 'request_logs', ['id'], unique=False)
    # ### end Alembic commands ###
