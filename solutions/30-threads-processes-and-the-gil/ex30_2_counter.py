"""Reference solution for exercise 30-2 (Threads, processes and the GIL)."""

import threading


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
        self._lock = threading.Lock()
        self._count = 0

    def increment(self) -> None:
        with self._lock:
            self._count += 1

    @property
    def value(self) -> int:
        with self._lock:
            return self._count
