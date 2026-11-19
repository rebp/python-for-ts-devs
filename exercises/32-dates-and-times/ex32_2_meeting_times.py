"""Lesson 32 · Dates and times · exercise 2.

Check your work with: uv run course.py
"""

from datetime import datetime
from zoneinfo import ZoneInfo  # noqa: F401


def local_times(meeting: datetime, zones: list[str]) -> dict[str, str]:
    """Show a meeting time, stored in UTC, as local "HH:MM" in each zone.

        meeting = datetime(2026, 3, 27, 15, 0, tzinfo=UTC)
        local_times(meeting, ["Europe/Madrid", "America/New_York"])
        -> {"Europe/Madrid": "16:00", "America/New_York": "11:00"}

    Zone names are IANA names, the same ones Intl.DateTimeFormat's timeZone
    option takes. Daylight saving time must be right: Europe moves its
    clocks on 29 March 2026, so the same 15:00 UTC meeting on 30 March is
    17:00 in Madrid.

    - Keep the zones in the order they were given.
    - A naive datetime (tzinfo is None) has no fixed instant: raise ValueError.

    Hint: meeting.astimezone(ZoneInfo(name)), then .strftime("%H:%M").
    """
    raise NotImplementedError("Your code here")
