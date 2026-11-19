"""Tests for exercise 08-1 (Scope and the mutable default trap).

Edit: ex08_1_mutable_default.py::add_tag
"""

import inspect

from ex08_1_mutable_default import add_tag


def test_calls_without_tags_do_not_share_a_list():
    assert add_tag("a") == ["a"]
    assert add_tag("b") == ["b"]


def test_default_is_none():
    assert inspect.signature(add_tag).parameters["tags"].default is None


def test_appends_to_a_list_you_pass():
    existing = ["x"]
    result = add_tag("y", existing)
    assert result is existing
    assert existing == ["x", "y"]
