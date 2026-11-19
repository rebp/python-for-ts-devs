"""Tests for exercise 28-2 (Context managers).

Edit: ex28_2_cd.py::cd
"""

import os
from pathlib import Path

import pytest
from ex28_2_cd import cd


def test_changes_and_restores(tmp_path):
    start = os.getcwd()
    with cd(str(tmp_path)):
        assert Path.cwd().resolve() == tmp_path.resolve()
    assert os.getcwd() == start


def test_restores_after_an_exception(tmp_path):
    start = os.getcwd()
    with pytest.raises(RuntimeError), cd(str(tmp_path)):
        raise RuntimeError("boom")
    assert os.getcwd() == start
