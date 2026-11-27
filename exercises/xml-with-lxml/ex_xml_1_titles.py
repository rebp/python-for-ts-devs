"""Lesson 9.2 · XML with lxml · exercise 1.

Check your work with: uv run course.py 9.2-1
"""


def section_titles(xml: bytes) -> list[str]:
    """Return each section title from an STS-like XML document, in order.

    The elements use the namespace ``urn:example:sts``. Titles can contain
    inline elements, so include all of their text. Parse the bytes without
    resolving entities or loading external resources.
    """
    raise NotImplementedError("Your code here")
