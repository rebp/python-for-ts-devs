"""Reference solution for exercise 32-1 (Dates and times)."""

from datetime import UTC, datetime


def from_iso(text: str) -> datetime:
    """Parse a timestamp sent by a JavaScript front end and return it as an
    aware datetime in UTC.

    JSON.stringify(new Date()) produces strings like "2026-03-29T00:30:00.000Z".
    Other clients may send an offset instead: "2026-03-29T02:30:00+02:00" is
    the same instant.

        from_iso("2026-03-29T00:30:00Z")
        -> datetime(2026, 3, 29, 0, 30, tzinfo=UTC)

    - Always return the result in UTC (use .astimezone(UTC)).
    - A string without a zone ("2026-03-29T00:30:00") is ambiguous: raise
      ValueError instead of guessing.

    Then write from_js_millis, below this function: it turns a Date.now()
    timestamp (milliseconds) into the same kind of UTC datetime.

    Hint: datetime.fromisoformat accepts the trailing "Z" since Python 3.11,
    and an aware datetime has a tzinfo that isn't None.
    """
    parsed = datetime.fromisoformat(text)
    if parsed.tzinfo is None:
        raise ValueError(f"timestamp has no time zone: {text}")
    return parsed.astimezone(UTC)


def from_js_millis(millis: int) -> datetime:
    """Convert a JavaScript timestamp (Date.now(), milliseconds since 1970)
    to an aware datetime in UTC.

        from_js_millis(1774744200000)
        -> datetime(2026, 3, 29, 0, 30, tzinfo=UTC)

    Python timestamps are in seconds, so divide by 1000 first, and pass
    tz=UTC to datetime.fromtimestamp so the result is aware.
    """
    return datetime.fromtimestamp(millis / 1000, tz=UTC)
