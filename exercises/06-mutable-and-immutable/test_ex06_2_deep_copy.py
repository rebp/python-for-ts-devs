"""Tests for exercise 06-2 (Mutable and immutable).

Edit: ex06_2_deep_copy.py::deep_copy_with_tag
"""

from ex06_2_deep_copy import deep_copy_with_tag

from course_helpers import calls_name


def test_copy_gets_the_tag():
    original = {"title": "Draft", "tags": ["a"]}
    assert deep_copy_with_tag(original, "b") == {"title": "Draft", "tags": ["a", "b"]}


def test_original_does_not_change():
    original = {"title": "Draft", "tags": ["a"]}
    copied = deep_copy_with_tag(original, "b")
    assert original == {"title": "Draft", "tags": ["a"]}
    assert copied["tags"] is not original["tags"]


def test_uses_deepcopy():
    assert calls_name(deep_copy_with_tag, "deepcopy")
