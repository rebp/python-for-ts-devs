"""Reference solution for exercise 22-1 (Testing with pytest)."""

import pytest
from slugify import slugify


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello World", "hello-world"),
        ("  Spaces   everywhere ", "spaces-everywhere"),
        ("Python 3!", "python-3"),
        ("Hello World, Python!", "hello-world-python"),
    ],
)
def test_slugify(text, expected):
    assert slugify(text) == expected
