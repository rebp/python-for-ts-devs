"""Tests for exercise 14-2 (Typing in depth).

Edit: ex14_2_sort_users.py::sort_users
"""

from typing import get_args

import pytest
from ex14_2_sort_users import Order, User, sort_users

from course_helpers import type_check_strict

MODULE = "ex14_2_sort_users"

# Each "type: ignore" must be needed: mypy --strict reports an unused one,
# so these lines check that mypy rejects "up" and a user without an age.
USAGE = """
from ex14_2_sort_users import User, sort_users

users: list[User] = [
    {"name": "Ada", "age": 36},
    {"name": "Grace", "age": 85, "email": "grace@example.com"},
]
oldest_first: list[User] = sort_users(users, "desc")
sort_users(users, "up")  # type: ignore[arg-type]
no_age: User = {"name": "Linus"}  # type: ignore[typeddict-item]
"""


USERS = [
    {"name": "Grace", "age": 85, "email": "grace@example.com"},
    {"name": "Ada", "age": 36},
    {"name": "Linus", "age": 54},
]


def names(users):
    return [user["name"] for user in users]


def test_ascending():
    assert names(sort_users(USERS, "asc")) == ["Ada", "Linus", "Grace"]


def test_descending():
    assert names(sort_users(USERS, "desc")) == ["Grace", "Linus", "Ada"]


def test_does_not_change_the_input():
    users = list(USERS)
    sort_users(users, "asc")
    assert names(users) == ["Grace", "Ada", "Linus"]


def test_unknown_order_raises_at_runtime():
    with pytest.raises(ValueError):
        sort_users(USERS, "up")


def test_order_is_a_literal():
    value = getattr(Order, "__value__", Order)  # works with `type Order = ...` too
    assert set(get_args(value)) == {"asc", "desc"}


def test_user_is_a_typeddict_with_optional_email():
    assert User.__required_keys__ == {"name", "age"}
    assert User.__optional_keys__ == {"email"}


def test_passes_mypy_strict(lesson_dir, tmp_path):
    ok, output = type_check_strict(lesson_dir / f"{MODULE}.py", USAGE, tmp_path)
    assert ok, "mypy --strict found problems:\n" + output
