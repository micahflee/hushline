"""empty message

Revision ID: dfeb75b32d3f
Revises:
Create Date: 2024-04-23 20:23:46.586664

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "dfeb75b32d3f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "invite_code",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("code", sa.String(length=255), nullable=False),
        sa.Column("expiration_date", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("primary_username", sa.String(length=80), nullable=False),
        sa.Column("display_name", sa.String(length=80), nullable=True),
        sa.Column("password_hash", sa.String(length=255), nullable=True),
        sa.Column("totp_secret", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("smtp_server", sa.String(length=255), nullable=True),
        sa.Column("smtp_port", sa.Integer(), nullable=True),
        sa.Column("smtp_username", sa.String(length=255), nullable=True),
        sa.Column("smtp_password", sa.String(length=255), nullable=True),
        sa.Column("pgp_key", sa.Text(), nullable=True),
        sa.Column("is_verified", sa.Boolean(), nullable=True),
        sa.Column("is_admin", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("primary_username"),
    )
    op.create_table(
        "secondary_usernames",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=80), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("display_name", sa.String(length=80), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "message",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("secondary_user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["secondary_user_id"],
            ["secondary_usernames.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("message")
    op.drop_table("secondary_usernames")
    op.drop_table("users")
    op.drop_table("invite_code")
    # ### end Alembic commands ###