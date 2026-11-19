"""Tests for exercise 04-2 (Control flow).

Edit: ex04_2_enumerate.py::print_ranking
"""

from ex04_2_enumerate import print_ranking

from course_helpers import calls_name


def test_prints_positions_from_one(capsys):
    print_ranking([72, 95, 48, 88])
    assert capsys.readouterr().out.splitlines() == ["1. 72", "2. 95", "3. 48", "4. 88"]


def test_empty_list_prints_nothing(capsys):
    print_ranking([])
    assert capsys.readouterr().out == ""


def test_uses_enumerate():
    assert calls_name(print_ranking, "enumerate"), (
        "loop with enumerate(scores, start=1)"
    )
