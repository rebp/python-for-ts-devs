"""Lesson 11 · Enums and match · exercise 3.

Check your work with: uv run course.py
"""

from enum import Enum


class Priority(Enum):
    """LOW, MEDIUM and HIGH, with the values "low", "medium" and "high"."""

    # TODO: add the three members


def days_to_respond(priority: Priority) -> int:
    """Create a Priority enum with LOW, MEDIUM and HIGH, and a function that returns
    how many days you have to respond: 5, 2 and 0.

    Give the members the values "low", "medium" and "high", so that
    Priority("medium") is Priority.MEDIUM. Use match in days_to_respond.
    """
    raise NotImplementedError("Your code here")
