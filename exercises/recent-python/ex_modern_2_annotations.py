"""Lesson 13.3 · What's new in Python 3.13–3.15 · exercise 2.

Check your work with: uv run course.py 13.3-2
"""

from collections.abc import Callable


def unresolved_annotations(function: Callable[..., object]) -> list[str]:
    """Return parameter names with top-level unresolved forward annotations.

    Use annotationlib's FORWARDREF format. Preserve annotation order and
    exclude resolved types.
    """
    raise NotImplementedError("Your code here")
