"""Tests for exercise 18-3 (Exceptions).

Edit: ex18_3_sum_valid.py::sum_valid
"""

from ex18_3_sum_valid import sum_valid


def test_skips_and_warns(capsys):
    assert sum_valid(["1", "x", "3", ""]) == 4
    assert capsys.readouterr().out.splitlines() == ["skipping 'x'", "skipping ''"]


def test_all_valid(capsys):
    assert sum_valid(["10", "-2"]) == 8
    assert capsys.readouterr().out == ""
