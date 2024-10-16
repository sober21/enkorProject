"""create tables orders

Revision ID: b37e4801f854
Revises: 781ec703d237
Create Date: 2024-10-10 17:13:59.115419

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b37e4801f854'
down_revision: Union[str, None] = '781ec703d237'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_name', sa.String(length=50), nullable=False),
    sa.Column('count_positions', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('add_date', sa.DATETIME(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_orders_employee_id_employees')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###
