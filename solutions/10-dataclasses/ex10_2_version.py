"""Reference solution for exercise 10-2 (Dataclasses)."""

from dataclasses import dataclass


@dataclass(order=True)
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
    return sorted(versions)
