"""Lesson 10 · Dataclasses · exercise 3.

Check your work with: uv run course.py
"""

from dataclasses import dataclass


@dataclass
class Point:
    """Make Point frozen, then try p.x = 5 and read the error.

    Frozen dataclasses are immutable, so they're also hashable: you can put
    points in a set or use them as dict keys.
    """

    x: float
    y: float
