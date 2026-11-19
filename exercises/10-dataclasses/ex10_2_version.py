"""Lesson 10 · Dataclasses · exercise 2.

Check your work with: uv run course.py
"""

from dataclasses import dataclass


@dataclass
class Version:
    major: int
    minor: int
    patch: int


def sort_versions(versions: list[Version]) -> list[Version]:
    """Create Version(major, minor, patch) with order=True and sort
    [Version(1, 10, 0), Version(1, 2, 3), Version(0, 9, 9)].

    The Version dataclass is started for you: make it ordered. Then
    sort_versions returns a new, sorted list: 0.9.9, 1.2.3, 1.10.0.
    """
    raise NotImplementedError("Your code here")
