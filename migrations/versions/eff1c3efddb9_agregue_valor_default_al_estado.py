"""agregue valor default al estado

Revision ID: eff1c3efddb9
Revises: 97770775b4ac
Create Date: 2024-02-11 21:37:11.373447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eff1c3efddb9'
down_revision = '97770775b4ac'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='pedidos', column_name='estado',
                    server_default='EN_ESPERA')


def downgrade():
    op.alter_column(table_name='pedidos', column_name='estado',
                    server_default=None)
