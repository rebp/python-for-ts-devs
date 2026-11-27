"""Lesson 3.7 · The data model · exercise 2.

Check your work with: uv run course.py 3.7-2
"""

from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class CaseKey:
    """A hashable key whose names compare without regard to case."""

    name: str

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("Your code here")

    def __hash__(self) -> int:
        raise NotImplementedError("Your code here")
