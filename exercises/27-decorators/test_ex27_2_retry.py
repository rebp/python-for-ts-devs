"""Tests for exercise 27-2 (Decorators).

Edit: ex27_2_retry.py::retry
"""

import pytest
from ex27_2_retry import retry


def make_flaky(failures):
    calls = []

    def flaky(value):
        calls.append(value)
        if len(calls) <= failures:
            raise ConnectionError("try again")
        return value * 2

    return flaky, calls


def test_succeeds_after_failures():
    flaky, calls = make_flaky(failures=2)
    assert retry(times=3)(flaky)(21) == 42
    assert len(calls) == 3


def test_reraises_after_the_last_attempt():
    flaky, calls = make_flaky(failures=10)
    with pytest.raises(ConnectionError):
        retry(times=3)(flaky)(1)
    assert len(calls) == 3


def test_default_is_three_attempts():
    flaky, calls = make_flaky(failures=10)
    with pytest.raises(ConnectionError):
        retry()(flaky)(1)
    assert len(calls) == 3


def test_keeps_the_name():
    @retry(times=2)
    def fetch():
        return "ok"

    assert fetch() == "ok"
    assert fetch.__name__ == "fetch"
