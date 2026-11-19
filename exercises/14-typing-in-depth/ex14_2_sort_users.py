"""Lesson 14 · Typing in depth · exercise 2.

Check your work with: uv run course.py
"""

from typing import Literal, NotRequired, TypedDict  # noqa: F401

# TODO: replace these two placeholders with real types
type Order = str
type User = dict[str, object]


def sort_users(users: list[User], order: Order) -> list[User]:
    """Type a function that sorts JSON-shaped users by age.

    In TypeScript you'd write:

        type Order = "asc" | "desc";
        interface User { name: string; age: number; email?: string }

    1. Replace the placeholder Order with a type alias for Literal["asc", "desc"]
       (use the type statement: type Order = ...).
    2. Replace the placeholder User with a TypedDict: name (str) and age (int)
       are required, email (str) is optional, using NotRequired.
    3. sort_users returns a new list sorted by age, youngest first for "asc"
       and oldest first for "desc". Don't change the list passed in.

    Type hints aren't checked when the code runs, so a caller can still pass
    "up". Raise ValueError for any order other than "asc" or "desc".
    The tests run mypy --strict too, and check that mypy rejects "up" and a
    user without an age.
    """
    raise NotImplementedError("Your code here")
