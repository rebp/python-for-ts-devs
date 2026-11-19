"""Reference solution for exercise 11-1 (Enums and match)."""

import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float


@dataclass
class Rect:
    w: float
    h: float


@dataclass
class Triangle:
    """Add a Triangle(base, height) dataclass and support it in area().

    area(Triangle(base=3, height=4)) returns 6.0. Circles and rectangles keep
    working, and anything else still raises TypeError.
    """

    base: float
    height: float


def area(shape: Circle | Rect | Triangle) -> float:
    match shape:
        case Circle(radius=r):
            return math.pi * r**2
        case Rect(w=w, h=h):
            return w * h
        case Triangle(base=b, height=h):
            return b * h / 2
        case _:
            raise TypeError(f"unknown shape: {shape}")
