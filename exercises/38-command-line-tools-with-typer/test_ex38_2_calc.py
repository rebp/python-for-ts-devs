"""Tests for exercise 38-2 (Command-line tools with Typer).

Edit: ex38_2_calc.py::add
"""

import re

from ex38_2_calc import app
from typer.testing import CliRunner

runner = CliRunner()


def plain(text):
    """Typer's --help output may contain color codes (for example when
    FORCE_COLOR is set, or on CI). Strip them so the checks see plain text."""
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def run(*args):
    return runner.invoke(app, list(args))


def test_add():
    result = run("add", "2", "3")
    assert result.exit_code == 0, result.output
    assert result.stdout == "5\n"


def test_add_decimals():
    assert run("add", "2.5", "0.25").stdout == "2.75\n"


def test_divide():
    result = run("divide", "7", "2")
    assert result.exit_code == 0, result.output
    assert result.stdout == "3.5\n"


def test_divide_by_zero_fails_with_a_message_on_stderr():
    result = run("divide", "1", "0")
    assert result.exit_code == 1
    assert "can't divide by zero" in result.stderr
    assert result.stdout == ""


def test_the_command_name_is_required():
    assert run("2", "3").exit_code == 2


def test_help_lists_both_commands():
    result = run("--help")
    assert result.exit_code == 0
    assert "add" in plain(result.output)
    assert "divide" in plain(result.output)
