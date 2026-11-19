"""Tests for exercise 16-1 (Strings in depth).

Edit: ex16_1_slugify.py::slugify
"""

import pytest
from ex16_1_slugify import slugify


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World, Python!", "hello-world-python"),
        ("  Spaces   everywhere ", "spaces-everywhere"),
        ("Python 3!", "python-3"),
        ("", ""),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
