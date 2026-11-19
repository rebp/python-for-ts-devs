"""Reference solution for exercise 32-3 (Dates and times)."""

from datetime import date, timedelta


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
    if days < 0:
        raise ValueError("days must be zero or positive")
    current = start
    remaining = days
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:
            remaining -= 1
    return current
