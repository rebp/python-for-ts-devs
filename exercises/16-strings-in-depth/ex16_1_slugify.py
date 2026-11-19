"""Lesson 16 · Strings in depth · exercise 1.

Check your work with: uv run course.py
"""


def slugify(text: str) -> str:
    """Write slugify(text) so that slugify("Hello World, Python!") returns
    "hello-world-python".

    Lowercase everything, drop punctuation, keep letters and digits, and join
    the words with single hyphens.

    Hint: keep characters where ch.isalnum() or ch.isspace(), then split() and
    join with hyphens.
    """
    raise NotImplementedError("Your code here")
