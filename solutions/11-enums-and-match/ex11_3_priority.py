"""Reference solution for exercise 11-3 (Enums and match)."""

from enum import Enum


class Priority(Enum):
    """LOW, MEDIUM and HIGH, with the values "low", "medium" and "high"."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


def days_to_respond(priority: Priority) -> int:
    """Create a Priority enum with LOW, MEDIUM and HIGH, and a function that returns
    how many days you have to respond: 5, 2 and 0.

    Give the members the values "low", "medium" and "high", so that
    Priority("medium") is Priority.MEDIUM. Use match in days_to_respond.
    """
    match priority:
        case Priority.LOW:
            return 5
        case Priority.MEDIUM:
            return 2
        case Priority.HIGH:
            return 0
