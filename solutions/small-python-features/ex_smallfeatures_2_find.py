"""Reference solution for exercise 4.4-2."""

from collections.abc import Iterable


def find_index(values: Iterable[str], target: str) -> int | None:
    """Return the first match, or None if the loop completes."""
    for index, value in enumerate(values):
        if value == target:
            break
    else:
        return None
    return index
