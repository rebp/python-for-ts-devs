"""Tests for exercise 29-2 (Async and await).

Edit: ex29_2_sequential.py::run_one_by_one
"""

import asyncio

from ex29_2_sequential import run_one_by_one


def test_runs_one_after_another(capsys):
    elapsed = asyncio.run(run_one_by_one(0.1))
    assert capsys.readouterr().out.split() == ["a", "b", "c"]
    assert 0.28 < elapsed < 0.6, "three 0.1 s sleeps in a row should take about 0.3 s"
