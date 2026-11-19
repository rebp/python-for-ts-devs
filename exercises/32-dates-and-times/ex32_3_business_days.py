"""Lesson 32 · Dates and times · exercise 3.

Check your work with: uv run course.py
"""

from datetime import date, timedelta  # noqa: F401


def add_business_days(start: date, days: int) -> date:
    """Return the date that is `days` business days (Monday to Friday) after
    `start`, skipping weekends.

        add_business_days(date(2026, 11, 20), 1)   # a Friday
        -> date(2026, 11, 23)                      # the next Monday

    - days=0 returns start unchanged.
    - Starting on a weekend works too: Saturday + 1 business day is Monday.
    - Negative days raise ValueError.

    Hint: step one day at a time with timedelta(days=1). date.weekday()
    returns 0 for Monday up to 6 for Sunday, unlike JavaScript's getDay(),
    where 0 is Sunday.
    """
    raise NotImplementedError("Your code here")
