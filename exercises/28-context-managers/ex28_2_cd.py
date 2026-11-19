"""Lesson 28 · Context managers · exercise 2.

Check your work with: uv run course.py
"""

from contextlib import contextmanager


@contextmanager
def cd(path: str):
    """Write a @contextmanager called cd(path) that changes the working directory
    and always changes back.

    Inside `with cd(path):` the working directory is path. Afterwards it's the
    previous one again, even when the block raised an exception.

    Hint: os.getcwd() and os.chdir(); put the yield inside try/finally.
    """
    raise NotImplementedError("Your code here")
