"""Tests for exercise 10.3-1.

Edit: ex_postgres_1_query.py::active_users_in_region
"""

from ex_postgres_1_query import active_users_in_region
from sqlalchemy.dialects import postgresql


def test_jsonb_query_uses_bound_values() -> None:
    region = "north'; DROP TABLE users; --"
    compiled = active_users_in_region(region).compile(dialect=postgresql.dialect())
    sql = str(compiled)
    assert "@>" in sql
    assert "->>" in sql
    assert region not in sql
    assert region in compiled.params.values()
    assert {"active": True} in compiled.params.values()


def test_region_is_not_hard_coded() -> None:
    compiled = active_users_in_region("south").compile(dialect=postgresql.dialect())
    assert "south" in compiled.params.values()
