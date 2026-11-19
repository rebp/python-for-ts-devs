"""Tests for exercise 30-2 (Threads, processes and the GIL).

Edit: ex30_2_counter.py::Counter
"""

import threading

import pytest
from ex30_2_counter import Counter


class RecordingLock:
    """Stands in for threading.Lock and records whether it was held."""

    def __init__(self) -> None:
        self.held = False
        self.acquired = 0

    def __enter__(self):
        assert not self.held, "the lock was acquired twice without being released"
        self.held = True
        self.acquired += 1
        return self

    def __exit__(self, *exc_info):
        self.held = False
        return False


def test_starts_at_zero():
    assert Counter().value == 0


def test_increment():
    counter = Counter()
    counter.increment()
    counter.increment()
    assert counter.value == 2


def test_stores_a_lock():
    assert isinstance(Counter()._lock, type(threading.Lock()))


def test_increment_holds_the_lock():
    counter = Counter()
    counter._lock = RecordingLock()
    counter.increment()
    assert counter._lock.acquired == 1, "increment() should use: with self._lock:"
    assert not counter._lock.held
    assert counter.value == 1


def test_value_is_read_only():
    with pytest.raises(AttributeError):
        Counter().value = 5


def test_many_threads():
    counter = Counter()

    def work():
        for _ in range(10_000):
            counter.increment()

    threads = [threading.Thread(target=work) for _ in range(8)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert counter.value == 80_000
