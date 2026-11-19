"""Tests for exercise 27-3 (Decorators).

Edit: ex27_3_cache.py::fib
"""

from ex27_3_cache import fib


def test_small_values():
    assert [fib(n) for n in range(10)] == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_fib_32():
    assert fib(32) == 2178309


def test_is_cached():
    assert hasattr(fib, "cache_info"), "decorate fib with @functools.cache"
    assert fib(200) == 280571172992510140037611932413038677189525
