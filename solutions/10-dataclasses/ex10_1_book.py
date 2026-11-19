"""Reference solution for exercise 10-1 (Dataclasses)."""

from dataclasses import dataclass, field


@dataclass
class Book:
    """Create a Book dataclass with title, author, year and a tags list that
    defaults to empty.

    Book("Dune", "Frank Herbert", 1965).tags is [], and two books must never
    share the same tags list.

    Hint: a list default needs field(default_factory=list).
    """

    title: str
    author: str
    year: int
    tags: list[str] = field(default_factory=list)
