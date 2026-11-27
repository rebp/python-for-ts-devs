"""Reference solution for exercise 10.3-1."""

from sqlalchemy import Column, Integer, MetaData, Table, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import Select

users = Table(
    "users",
    MetaData(),
    Column("id", Integer, primary_key=True),
    Column("profile", JSONB, nullable=False),
)


def active_users_in_region(region: str) -> Select[tuple[int]]:
    """Build a parameterized JSONB query."""
    return select(users.c.id).where(
        users.c.profile.contains({"active": True}),
        users.c.profile["region"].as_string() == region,
    )
