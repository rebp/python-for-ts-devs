"""Reference solution for exercise 26-2 (Iterators and generators)."""

from collections.abc import Iterator


def read_lines(path: str) -> Iterator[str]:
    """Write read_lines(path) that yields each line of a text file, stripped,
    skipping empty lines.

    Open the file with `with open(path, encoding="utf-8") as f:` and yield
    from inside the with block.
    """
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield line
