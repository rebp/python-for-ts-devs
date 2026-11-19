"""Lesson 26 · Iterators and generators · exercise 2.

Check your work with: uv run course.py
"""

from collections.abc import Iterator


def read_lines(path: str) -> Iterator[str]:
    """Write read_lines(path) that yields each line of a text file, stripped,
    skipping empty lines.

    Open the file with `with open(path, encoding="utf-8") as f:` and yield
    from inside the with block.
    """
    raise NotImplementedError("Your code here")
