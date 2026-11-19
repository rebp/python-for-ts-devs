"""Lesson 14 · Typing in depth · exercise 1.

Check your work with: uv run course.py
"""

from collections.abc import Callable, Iterable  # noqa: F401


def group_by(items, key):
    """Write a generic group_by(items, key), like lodash's groupBy, fully typed.

    group_by(["apple", "avocado", "banana"], lambda word: word[0]) returns
    {"a": ["apple", "avocado"], "b": ["banana"]}, keeping the original order
    inside each group. group_by([], len) returns {}.

    The types must carry through, so mypy knows that
    group_by(["a", "bb"], len) is a dict[int, list[str]]:

    - items is any Iterable of some type T (a list, a generator...),
    - key is a Callable that takes a T and returns some key type K,
    - the result is a dict[K, list[T]].

    Use the Python 3.12 generic syntax: def group_by[T, K](...). The tests
    also run mypy --strict on your file, so don't leave anything as Any.
    """
    raise NotImplementedError("Your code here")
