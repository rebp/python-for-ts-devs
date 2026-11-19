"""Lesson 11 · Enums and match · exercise 1.

Check your work with: uv run course.py
"""

import math
from dataclasses import dataclass


@dataclass
class Circle:
    radius: float


@dataclass
class Rect:
    w: float
    h: float


class Triangle:
    """Add a Triangle(base, height) dataclass and support it in area().

    area(Triangle(base=3, height=4)) returns 6.0. Circles and rectangles keep
    working, and anything else still raises TypeError.
    """

    # TODO: make this a dataclass with base and height


def area(shape: Circle | Rect) -> float:
    match shape:
        case Circle(radius=r):
            return math.pi * r**2
        case Rect(w=w, h=h):
            return w * h
        case _:
            raise TypeError(f"unknown shape: {shape}")
