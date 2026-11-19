"""Tests for exercise 29-3 (Async and await).

Edit: ex29_3_timeout.py::slow_with_timeout
"""

import asyncio
import time

from ex29_3_timeout import slow_with_timeout


def test_times_out(capsys):
    start = time.perf_counter()
    assert asyncio.run(slow_with_timeout(5, 0.1)) is False
    assert time.perf_counter() - start < 1, "it should stop waiting after the timeout"
    out = capsys.readouterr().out
    assert "gave up after 0.1 second" in out
    assert "slow" not in out


def test_finishes_in_time(capsys):
    assert asyncio.run(slow_with_timeout(0.01, 1)) is True
    assert capsys.readouterr().out == "slow\n"
