"""Lesson 10.3 · Postgres for real · exercise 1.

Check your work with: uv run course.py 10.3-1
"""

from sqlalchemy import Column, Integer, MetaData, Table
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import Select

users = Table(
    "users",
    MetaData(),
    Column("id", Integer, primary_key=True),
    Column("profile", JSONB, nullable=False),
)


def active_users_in_region(region: str) -> Select[tuple[int]]:
    """Build a parameterized query selecting IDs of active users in a region.

    The JSONB profile has an ``active`` boolean and a ``region`` string.
    Build the statement only; do not connect to a database.
    """
    raise NotImplementedError("Your code here")
