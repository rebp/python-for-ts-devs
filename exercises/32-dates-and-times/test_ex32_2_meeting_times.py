"""Tests for exercise 32-2 (Dates and times).

Edit: ex32_2_meeting_times.py::local_times
"""

from datetime import UTC, datetime

import pytest
from ex32_2_meeting_times import local_times

ZONES = ["Europe/Madrid", "Europe/London", "America/New_York", "Asia/Tokyo"]


def test_before_the_european_clock_change():
    meeting = datetime(2026, 3, 27, 15, 0, tzinfo=UTC)
    assert local_times(meeting, ZONES) == {
        "Europe/Madrid": "16:00",
        "Europe/London": "15:00",
        "America/New_York": "11:00",
        "Asia/Tokyo": "00:00",
    }


def test_after_the_european_clock_change():
    meeting = datetime(2026, 3, 30, 15, 0, tzinfo=UTC)
    assert local_times(meeting, ZONES) == {
        "Europe/Madrid": "17:00",
        "Europe/London": "16:00",
        "America/New_York": "11:00",
        "Asia/Tokyo": "00:00",
    }


def test_keeps_the_order_of_the_zones():
    meeting = datetime(2026, 3, 27, 15, 0, tzinfo=UTC)
    assert list(local_times(meeting, ["Asia/Tokyo", "Europe/Madrid"])) == [
        "Asia/Tokyo",
        "Europe/Madrid",
    ]


def test_rejects_naive_datetimes():
    with pytest.raises(ValueError):
        local_times(datetime(2026, 3, 27, 15, 0), ZONES)
