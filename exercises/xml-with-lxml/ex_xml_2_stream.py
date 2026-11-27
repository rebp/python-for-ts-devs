"""Lesson 9.2 · XML with lxml · exercise 2.

Check your work with: uv run course.py 9.2-2
"""

from pathlib import Path


def count_sections(path: Path) -> int:
    """Count STS-like sections in a file without retaining the whole tree.

    Match ``sec`` elements in ``urn:example:sts``. Use end events from
    ``iterparse``, clear each processed element and discard preceding
    siblings. Disable entity resolution, DTD loading and network access.
    """
    raise NotImplementedError("Your code here")
