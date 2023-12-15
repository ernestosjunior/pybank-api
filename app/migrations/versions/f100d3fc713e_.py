"""empty message

Revision ID: f100d3fc713e
Revises: 
Create Date: 2023-12-14 21:37:19.369461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f100d3fc713e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("cpf", sa.String(length=11), nullable=False),
        sa.Column("birth_date", sa.DateTime(), nullable=False),
        sa.Column("email", sa.String(length=80), nullable=False),
        sa.Column("password", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("cpf"),
        sa.UniqueConstraint("email"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
