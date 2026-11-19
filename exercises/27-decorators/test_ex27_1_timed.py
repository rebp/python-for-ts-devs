"""Tests for exercise 27-1 (Decorators).

Edit: ex27_1_timed.py::timed
"""

import re
import time

from ex27_1_timed import timed


def test_returns_the_result_and_prints_the_time(capsys):
    @timed
    def add(a, b):
        return a + b

    assert add(2, b=3) == 5
    assert re.fullmatch(r"add took \d+\.\d{4}s\n", capsys.readouterr().out)


def test_measures_the_real_time(capsys):
    @timed
    def nap():
        time.sleep(0.05)

    nap()
    seconds = float(re.search(r"took ([\d.]+)s", capsys.readouterr().out).group(1))
    assert 0.04 < seconds < 1


def test_keeps_the_name():
    @timed
    def report():
        """Docs."""

    assert report.__name__ == "report"
    assert report.__doc__ == "Docs."
