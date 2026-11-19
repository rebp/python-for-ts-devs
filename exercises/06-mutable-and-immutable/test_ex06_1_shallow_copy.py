"""Tests for exercise 06-1 (Mutable and immutable).

Edit: ex06_1_shallow_copy.py::shallow_copy_with_tag
"""

from ex06_1_shallow_copy import shallow_copy_with_tag


def test_returns_a_new_dict_with_the_tag():
    original = {"title": "Draft", "tags": ["a"]}
    copied = shallow_copy_with_tag(original, "b")
    assert copied is not original
    assert copied == {"title": "Draft", "tags": ["a", "b"]}


def test_the_tags_list_is_shared():
    original = {"title": "Draft", "tags": ["a"]}
    copied = shallow_copy_with_tag(original, "b")
    assert original["tags"] == ["a", "b"], "a shallow copy shares the nested list"
    assert copied["tags"] is original["tags"]
