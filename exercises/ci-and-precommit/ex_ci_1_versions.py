"""Lesson 11.2 · CI and pre-commit · exercise 1.

Check your work with: uv run course.py 11.2-1
"""

from collections.abc import Iterable


def select_versions(versions: Iterable[str], minimum: str) -> list[str]:
    """Keep Python major.minor versions at or above minimum, in input order.

    Compare numeric components, not strings or floats. Reject malformed
    version strings with ValueError.
    """
    raise NotImplementedError("Your code here")
