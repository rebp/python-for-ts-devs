"""Lesson 06 · Mutable and immutable · exercise 3.

Check your work with: uv run course.py
"""


def try_as_key(key: object) -> str:
    """Try to use (1, 2) and then [1, 2] as a key in a dict. Which one fails, and why?

    try_as_key(key) tries grid[key] = "tree" on an empty dict. It returns "ok"
    when that works, or the name of the exception class when it fails
    (type(err).__name__).

    Hint: wrap the assignment in try: ... except TypeError as err: ...
    (lesson 18 covers exceptions properly; this is all you need for now).
    """
    raise NotImplementedError("Your code here")
