"""Reference solution for exercise 13-1 (Protocols and Pydantic)."""

from typing import Protocol


class Sized(Protocol):
    """Anything with a size() -> int method."""

    def size(self) -> int: ...


class Folder:
    """A folder; its size is the number of files in it."""

    def size(self) -> int:
        return 3


class Photo:
    """A photo; its size is in kilobytes."""

    def size(self) -> int:
        return 2048


def total_size(items: list[Sized]) -> int:
    """Define a Protocol called Sized with a size(self) -> int method, and two
    unrelated classes that satisfy it without inheriting from it.

    Folder() and Photo() take no arguments and each has a size() method that
    returns an int. total_size(items) adds up the sizes of anything that has a
    size() method.
    """
    return sum(item.size() for item in items)
