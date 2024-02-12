"""modificar estado a los pedidos antiguos

Revision ID: 07ebeaafba29
Revises: eff1c3efddb9
Create Date: 2024-02-11 21:43:08.000792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07ebeaafba29'
down_revision = 'eff1c3efddb9'
branch_labels = None
depends_on = None


def upgrade():
    # si queremos realizar en la migracion un comando de ejecucion SQL podemos usar el metodo execute
    op.execute("UPDATE pedidos SET estado = 'EN_ESPERA' WHERE estado IS NULL")


def downgrade():
    pass
