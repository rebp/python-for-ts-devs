"""Reference solution for exercise 06-3 (Mutable and immutable)."""


def try_as_key(key: object) -> str:
    """Try to use (1, 2) and then [1, 2] as a key in a dict. Which one fails, and why?

    try_as_key(key) tries grid[key] = "tree" on an empty dict. It returns "ok"
    when that works, or the name of the exception class when it fails
    (type(err).__name__).

    Hint: wrap the assignment in try: ... except TypeError as err: ...
    (lesson 18 covers exceptions properly; this is all you need for now).
    """
    grid = {}
    try:
        grid[key] = "tree"
    except TypeError as err:
        # Lists are mutable, so they aren't hashable and can't be dict keys.
        return type(err).__name__
    return "ok"
