"""Tests for exercise 03-2 (Functions).

Edit: ex03_2_average.py::average
"""

from ex03_2_average import average


def test_several_numbers():
    assert average(1, 2, 3) == 2
    assert average(1, 2) == 1.5


def test_one_number():
    assert average(7) == 7


def test_no_arguments_returns_zero():
    assert average() == 0


def test_spread_a_list():
    assert average(*[10, 20, 30, 40]) == 25
