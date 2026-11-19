"""Lesson 06 · Mutable and immutable · exercise 1.

Check your work with: uv run course.py
"""


def shallow_copy_with_tag(original: dict, tag: str) -> dict:
    """Make a shallow copy of {"title": "Draft", "tags": ["a"]}, append "b" to the
    copy's tags, and print the original. Explain what you see.

    shallow_copy_with_tag(original, tag) makes a shallow copy of the dict,
    appends tag to the copy's "tags" list and returns the copy. The tests then
    look at the original: it changed too. Why?
    """
    raise NotImplementedError("Your code here")
