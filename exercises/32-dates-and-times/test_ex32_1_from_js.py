"""Tests for exercise 32-1 (Dates and times).

Edit: ex32_1_from_js.py::from_iso
"""

from datetime import UTC, datetime

import pytest
from ex32_1_from_js import from_iso, from_js_millis

EXPECTED = datetime(2026, 3, 29, 0, 30, tzinfo=UTC)


def test_parses_z_suffix():
    assert from_iso("2026-03-29T00:30:00Z") == EXPECTED


def test_parses_milliseconds_from_json_stringify():
    assert from_iso("2026-03-29T00:30:00.000Z") == EXPECTED


def test_converts_offsets_to_utc():
    result = from_iso("2026-03-29T02:30:00+02:00")
    assert result == EXPECTED
    assert result.utcoffset().total_seconds() == 0
    assert result.hour == 0


def test_result_is_aware():
    assert from_iso("2026-03-29T00:30:00Z").tzinfo is not None


def test_rejects_naive_timestamps():
    with pytest.raises(ValueError):
        from_iso("2026-03-29T00:30:00")


def test_from_js_millis():
    result = from_js_millis(1774744200000)
    assert result == EXPECTED
    assert result.tzinfo is not None
    assert result.utcoffset().total_seconds() == 0


def test_from_js_millis_keeps_milliseconds():
    assert from_js_millis(1774744200250).microsecond == 250_000
