"""Lesson 22 · Testing with pytest · exercise 1.

Write tests for your slugify from lesson 16, including one parametrized test
with at least three cases.

slugify is imported from slugify.py in this folder. Your tests should notice
a slugify that forgets to lowercase, keeps punctuation, drops digits, or
turns repeated spaces into repeated hyphens.

How it's checked: your tests must pass against slugify.py, and fail against
broken versions of it. Run them yourself with:

    uv run pytest exercises/22-testing-with-pytest/ex22_1_slugify_tests.py

Check your work with: uv run course.py
"""

import pytest
from slugify import slugify  # noqa: F401  (delete this comment once you use slugify)


def test_placeholder():
    pytest.fail("Replace this placeholder with your own tests")
