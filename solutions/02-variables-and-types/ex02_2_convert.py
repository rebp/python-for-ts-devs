"""Reference solution for exercise 02-2 (Variables and types)."""


def add_eight(text: str) -> int:
    """Convert the string "42" to an int, add 8 and return the result.

    add_eight("42") returns 50 (the number, not the text "428").

    Then open the REPL (uv run python), try "42" + 8 and read the error
    message. JavaScript would happily give you "428".
    """
    return int(text) + 8
