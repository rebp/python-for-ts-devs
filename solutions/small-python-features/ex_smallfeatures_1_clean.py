"""Reference solution for exercise 4.4-1."""

from collections.abc import Iterable


def clean_lines(lines: Iterable[str]) -> list[str]:
    """Strip each line once and keep nonempty results."""
    return [cleaned for line in lines if (cleaned := line.strip())]
