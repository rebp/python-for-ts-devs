"""Tests for exercise 28-3 (Context managers).

Edit: ex28_3_timer_class.py::Timer
"""

import re
import time

import pytest
from ex28_3_timer_class import Timer


def test_prints_the_elapsed_time(capsys):
    with Timer("sleep") as timer:
        time.sleep(0.05)
    assert isinstance(timer, Timer), "__enter__ should return self"
    out = capsys.readouterr().out
    assert re.fullmatch(r"sleep: \d+\.\d{3}s\n", out)
    assert 0.04 < float(out.split(": ")[1][:-2]) < 1


def test_prints_and_reraises_on_error(capsys):
    with pytest.raises(ValueError), Timer("boom"):
        raise ValueError("bad")
    assert capsys.readouterr().out.startswith("boom: ")
