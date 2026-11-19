"""Tests for exercise 07-2 (Truthiness, None and equality).

Edit: ex07_2_get_port.py::get_port
"""

from ex07_2_get_port import get_port


def test_missing_port():
    assert get_port({}) == 8080


def test_port_set_to_none():
    assert get_port({"port": None}) == 8080


def test_configured_port():
    assert get_port({"port": 3000}) == 3000


def test_zero_is_a_valid_port():
    assert get_port({"port": 0}) == 0, "0 is falsy, so `or 8080` turns it into 8080"
