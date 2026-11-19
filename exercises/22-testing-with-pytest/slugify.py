"""The slugify function from lesson 16. Exercise 22-1 tests it."""


def slugify(text: str) -> str:
    cleaned = "".join(ch for ch in text.lower() if ch.isalnum() or ch.isspace())
    return "-".join(cleaned.split())
