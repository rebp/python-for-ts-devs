"""Lesson 28 · Context managers · exercise 3.

Check your work with: uv run course.py
"""


class Timer:
    """Write the timer example as a class with __enter__ and __exit__ instead of a
    generator.

    `with Timer("load"):` prints something like "load: 0.201s" (3 decimals) when
    the block ends, also when it raises. __enter__ returns the Timer itself, and
    exceptions from the block are not swallowed.
    """

    def __init__(self, label: str) -> None:
        self.label = label

    # TODO: __enter__ and __exit__
