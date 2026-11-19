"""Lesson 30 · Threads, processes and the GIL · exercise 3.

Check your work with: uv run course.py
"""

import time


def load_report(report_id: int) -> str:
    """A blocking call from a library with no async version. Don't change it."""
    time.sleep(0.3)
    return f"report {report_id}"


async def load_reports(report_ids: list[int]) -> dict[int, str]:
    """Load every report with the blocking load_report() from async code,
    without blocking the event loop, and return {report_id: report}.

    load_reports([1, 2]) returns {1: "report 1", 2: "report 2"}.

    Calling load_report() directly inside async code would freeze the event
    loop for 0.3 seconds per report, so nothing else could run (lesson 29).
    Run each call in a worker thread with asyncio.to_thread(load_report, id),
    and start them all together with asyncio.gather (or an asyncio.TaskGroup).
    Five reports should take about 0.3 seconds, not 1.5.
    """
    raise NotImplementedError("Your code here")
