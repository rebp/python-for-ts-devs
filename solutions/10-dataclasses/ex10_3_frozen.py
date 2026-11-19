"""Reference solution for exercise 10-3 (Dataclasses)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    """Make Point frozen, then try p.x = 5 and read the error.

    Frozen dataclasses are immutable, so they're also hashable: you can put
    points in a set or use them as dict keys.
    """

    x: float
    y: float
