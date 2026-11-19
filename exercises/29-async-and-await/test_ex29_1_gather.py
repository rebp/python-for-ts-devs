"""Tests for exercise 29-1 (Async and await).

Edit: ex29_1_gather.py::say_after
"""

import asyncio
import inspect

from ex29_1_gather import run_together, say_after


def test_say_after_is_async_and_prints(capsys):
    assert inspect.iscoroutinefunction(say_after)
    asyncio.run(say_after("hi", 0.01))
    assert capsys.readouterr().out == "hi\n"


def test_run_together_runs_at_the_same_time(capsys):
    elapsed = asyncio.run(run_together(0.2))
    assert sorted(capsys.readouterr().out.split()) == ["a", "b", "c"]
    assert 0.15 < elapsed < 0.45, "three 0.2 s sleeps at once should take about 0.2 s"
