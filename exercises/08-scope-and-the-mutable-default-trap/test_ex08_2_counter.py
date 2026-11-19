"""Tests for exercise 08-2 (Scope and the mutable default trap).

Edit: ex08_2_counter.py::make_counter
"""

from ex08_2_counter import make_counter


def test_counts_up_from_one():
    counter = make_counter()
    assert [counter(), counter(), counter()] == [1, 2, 3]


def test_counters_are_independent():
    first = make_counter()
    second = make_counter()
    first()
    first()
    assert second() == 1
    assert first() == 3
