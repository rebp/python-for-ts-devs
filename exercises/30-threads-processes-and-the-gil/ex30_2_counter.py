"""Lesson 30 · Threads, processes and the GIL · exercise 2.

Check your work with: uv run course.py
"""

import threading  # noqa: F401  (you'll need threading.Lock)


class Counter:
    """A counter that many threads can increment at the same time.

    - Counter().value is 0.
    - increment() adds 1 and returns nothing.
    - value is a read-only property.

    self._count += 1 is really three steps (read, add, write), and another
    thread can run between them, so two increments can turn into one. Store a
    threading.Lock in self._lock in __init__, and hold it while you change or
    read the count:

        with self._lock:
            ...

    Node never needs this, because only one thread runs your JavaScript.
    """

    def __init__(self) -> None:
        raise NotImplementedError("Your code here")

    def increment(self) -> None:
        raise NotImplementedError("Your code here")

    @property
    def value(self) -> int:
        raise NotImplementedError("Your code here")
