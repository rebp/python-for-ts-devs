"""Reference solution for exercise 01-2 (Hello, Python)."""


def lived_in(city: str, year: int) -> str:
    """Store a city and a year in variables and build "I've lived in Lisbon since 2019"
    using an f-string.

    Return the sentence instead of printing it, so a test can check it:
    lived_in("Lisbon", 2019) returns "I've lived in Lisbon since 2019".
    Use a plain apostrophe (').
    """
    return f"I've lived in {city} since {year}"
