"""Tests for exercise 30-3 (Threads, processes and the GIL).

Edit: ex30_3_to_thread.py::load_reports
"""

import asyncio
import time

from ex30_3_to_thread import load_reports


def test_returns_every_report():
    result = asyncio.run(load_reports([1, 2, 3]))
    assert result == {1: "report 1", 2: "report 2", 3: "report 3"}


def test_empty():
    assert asyncio.run(load_reports([])) == {}


def test_runs_in_parallel():
    start = time.perf_counter()
    asyncio.run(load_reports([1, 2, 3, 4, 5]))
    elapsed = time.perf_counter() - start
    # One after the other would take 1.5 s. In parallel it's about 0.3 s.
    assert elapsed < 0.9, f"took {elapsed:.2f}s: are the reports loading in parallel?"


def test_event_loop_keeps_running():
    """A heartbeat task must keep ticking while the reports load."""

    async def main():
        ticks = 0
        done = False

        async def heartbeat():
            nonlocal ticks
            while not done:
                ticks += 1
                await asyncio.sleep(0.02)

        beat = asyncio.create_task(heartbeat())
        await asyncio.sleep(0)  # let the heartbeat start
        ticks_before = ticks
        await load_reports([1, 2, 3])
        done = True
        await beat
        return ticks - ticks_before

    ticks_during_load = asyncio.run(main())
    assert ticks_during_load >= 5, (
        "the event loop was blocked: call load_report through asyncio.to_thread"
    )
