"""Updates UserAchievement Model

Revision ID: 985fd03788fe
Revises: 324e428ae4ee
Create Date: 2023-05-16 19:23:08.748698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '985fd03788fe'
down_revision = '324e428ae4ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_achievements', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('achievement_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('id')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_achievements', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.INTEGER(), nullable=False))
        batch_op.alter_column('achievement_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###