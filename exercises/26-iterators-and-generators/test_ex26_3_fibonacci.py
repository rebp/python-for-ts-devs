"""Tests for exercise 26-3 (Iterators and generators).

Edit: ex26_3_fibonacci.py::fibonacci
"""

import inspect
from itertools import islice

from ex26_3_fibonacci import fibonacci, first_fibonacci

from course_helpers import calls_name

FIRST_TEN = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fibonacci_is_a_generator():
    assert inspect.isgeneratorfunction(fibonacci)
    assert list(islice(fibonacci(), 10)) == FIRST_TEN


def test_first_fibonacci():
    assert first_fibonacci(10) == FIRST_TEN
    assert first_fibonacci(0) == []


def test_first_fibonacci_uses_islice():
    assert calls_name(first_fibonacci, "islice")
