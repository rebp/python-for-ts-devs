"""Tests for exercise 6.5-2.

Edit: ex_profiling_2_queue.py::drain_queue
"""

from ex_profiling_2_queue import drain_queue

from course_helpers import calls_name


def test_preserves_fifo_order_and_input() -> None:
    values = [3, 1, 3]
    assert drain_queue(values) == [3, 1, 3]
    assert values == [3, 1, 3]
    assert drain_queue(iter(())) == []


def test_uses_a_deque() -> None:
    assert calls_name(drain_queue, "deque")
    assert calls_name(drain_queue, "popleft")
