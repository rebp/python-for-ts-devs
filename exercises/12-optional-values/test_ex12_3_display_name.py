"""Tests for exercise 12-3 (Optional values).

Edit: ex12_3_display_name.py::display_name
"""

from ex12_3_display_name import display_name


def test_nickname_wins():
    assert display_name({"nickname": "Ada", "name": "Augusta"}) == "Ada"


def test_falls_back_to_name():
    assert display_name({"name": "Augusta"}) == "Augusta"
    assert display_name({"nickname": None, "name": "Grace"}) == "Grace"


def test_anonymous():
    assert display_name({}) == "anonymous"
    assert display_name({"nickname": None, "name": None}) == "anonymous"
