"""Lesson 10 · Dataclasses · exercise 1.

Check your work with: uv run course.py
"""


class Book:
    """Create a Book dataclass with title, author, year and a tags list that
    defaults to empty.

    Book("Dune", "Frank Herbert", 1965).tags is [], and two books must never
    share the same tags list.

    Hint: a list default needs field(default_factory=list).
    """

    # TODO: make this a dataclass with the four fields
