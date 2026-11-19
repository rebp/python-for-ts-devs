"""Tests for exercise 24-2 (Debugging).

Edit: ex24_2_where_it_failed.py::where_it_failed
"""

import inspect

import pytest
from ex24_2_where_it_failed import root_cause, where_it_failed


class OrderError(Exception):
    pass


def to_cents(price):
    return int(price) * 100  # the line that fails


def parse_line(line):
    return to_cents(line.split(",")[1])


def load_order(line):
    try:
        return parse_line(line)
    except ValueError as err:
        raise OrderError(f"bad order line: {line!r}") from err


def load_order_carelessly(line):
    try:
        return parse_line(line)
    except ValueError:
        return {}["fallback"]  # a second error while handling the first


def caught(func, *args):
    with pytest.raises(Exception) as info:
        func(*args)
    return info.value


def line_of(func, text):
    lines, start = inspect.getsourcelines(func)
    return start + next(i for i, line in enumerate(lines) if text in line)


def test_innermost_frame():
    exc = caught(parse_line, "Lamp,24.50")
    assert where_it_failed(exc) == (
        "test_ex24_2_where_it_failed.py",
        line_of(to_cents, "the line that fails"),
        "to_cents",
    )


def test_reports_the_outer_exception_of_a_chain():
    exc = caught(load_order, "Lamp,24.50")
    _file_name, line, function = where_it_failed(exc)
    assert function == "load_order"
    assert line == line_of(load_order, "raise OrderError")


def test_never_raised_has_no_location():
    assert where_it_failed(ValueError("never raised")) is None


def test_root_cause_follows_from():
    exc = caught(load_order, "Lamp,24.50")
    assert isinstance(exc, OrderError)
    root = root_cause(exc)
    assert isinstance(root, ValueError)
    assert "24.50" in str(root)


def test_root_cause_follows_context():
    exc = caught(load_order_carelessly, "Lamp,24.50")
    assert isinstance(exc, KeyError)
    assert isinstance(root_cause(exc), ValueError)


def test_root_cause_without_chain():
    exc = ValueError("alone")
    assert root_cause(exc) is exc
