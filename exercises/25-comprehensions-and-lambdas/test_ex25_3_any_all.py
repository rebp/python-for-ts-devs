"""Tests for exercise 25-3 (Comprehensions and lambdas).

Edit: ex25_3_any_all.py::someone_failed
"""

from ex25_3_any_all import all_below_100, someone_failed

from course_helpers import calls_name


def test_course_example():
    scores = [72, 95, 48, 88]
    assert someone_failed(scores) is True
    assert all_below_100(scores) is True


def test_nobody_failed_and_one_perfect_score():
    scores = [50, 100]
    assert someone_failed(scores) is False
    assert all_below_100(scores) is False


def test_empty_list():
    assert someone_failed([]) is False
    assert all_below_100([]) is True


def test_uses_any_and_all():
    assert calls_name(someone_failed, "any")
    assert calls_name(all_below_100, "all")
