"""Reference solution for exercise 28-2 (Context managers)."""

import os
from contextlib import contextmanager


@contextmanager
def cd(path: str):
    """Write a @contextmanager called cd(path) that changes the working directory
    and always changes back.

    Inside `with cd(path):` the working directory is path. Afterwards it's the
    previous one again, even when the block raised an exception.

    Hint: os.getcwd() and os.chdir(); put the yield inside try/finally.
    """
    previous = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)
