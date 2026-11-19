"""Reference solution for exercise 02-3 (Variables and types)."""


def format_minutes(minutes: int) -> str:
    """Convert 135 minutes into the text "2 h 15 min" using // and %.

    format_minutes(135) returns "2 h 15 min".
    """
    return f"{minutes // 60} h {minutes % 60} min"
