"""Tests for exercise 26-1 (Iterators and generators).

Edit: ex26_1_evens.py::evens
"""

import inspect

from ex26_1_evens import evens


def test_is_a_generator_function():
    assert inspect.isgeneratorfunction(evens), "use yield"


def test_includes_the_limit():
    assert list(evens(10)) == [0, 2, 4, 6, 8, 10]


def test_odd_limit():
    assert list(evens(9)) == [0, 2, 4, 6, 8]
    assert list(evens(0)) == [0]


def test_is_lazy():
    gen = evens(1_000_000_000)
    assert next(gen) == 0
    assert next(gen) == 2
