"""Reference solution for exercise 24-2 (Debugging)."""

import traceback
from pathlib import Path


def where_it_failed(exc: BaseException) -> tuple[str, int, str] | None:
    """Return where an exception was raised: (file name, line number, function).

    That's the innermost frame, the last one in the traceback. For an error
    raised on line 9 of /app/shop/prices.py inside to_cents, the result is
    ("prices.py", 9, "to_cents"): only the file name, without its folder.

    An exception that was created but never raised has no traceback
    (exc.__traceback__ is None). Return None for it.

    Hint: traceback.extract_tb(exc.__traceback__) returns the frames, oldest
    first. Each one has .filename, .lineno and .name.
    """
    if exc.__traceback__ is None:
        return None
    frame = traceback.extract_tb(exc.__traceback__)[-1]
    return Path(frame.filename).name, frame.lineno or 0, frame.name


def root_cause(exc: BaseException) -> BaseException:
    """Follow an exception chain back to the error that started it.

    `raise OrderError(...) from err` stores err in __cause__ ("The above
    exception was the direct cause of the following exception"). An exception
    raised inside an except block without `from` stores the one being handled
    in __context__ ("During handling of the above exception, another exception
    occurred"). Follow __cause__ when it's set, otherwise __context__, until
    there's nothing left, and return that last exception. An exception without
    a chain is its own root cause.
    """
    while True:
        previous = exc.__cause__ or exc.__context__
        if previous is None:
            return exc
        exc = previous
