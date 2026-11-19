"""Tests for exercise 38-1 (Command-line tools with Typer).

Edit: ex38_1_greet.py::greet
"""

import re

from ex38_1_greet import app
from typer.testing import CliRunner

runner = CliRunner()


def plain(text):
    """Typer's --help output may contain color codes (for example when
    FORCE_COLOR is set, or on CI). Strip them so the checks see plain text."""
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def test_greets():
    result = runner.invoke(app, ["Ada"])
    assert result.exit_code == 0, result.output
    assert result.output == "Hello, Ada!\n"


def test_shout():
    result = runner.invoke(app, ["Ada", "--shout"])
    assert result.exit_code == 0, result.output
    assert result.output == "HELLO, ADA!\n"


def test_times():
    result = runner.invoke(app, ["Grace", "--times", "3"])
    assert result.exit_code == 0, result.output
    assert result.output == "Hello, Grace!\n" * 3


def test_name_is_required():
    assert runner.invoke(app, []).exit_code == 2


def test_times_must_be_a_number():
    assert runner.invoke(app, ["Ada", "--times", "abc"]).exit_code == 2


def test_help_lists_the_options():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--shout" in plain(result.output)
    assert "--times" in plain(result.output)
