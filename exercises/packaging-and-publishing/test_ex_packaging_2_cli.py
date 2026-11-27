"""Tests for exercise 11.3-2.

Edit: ex_packaging_2_cli.py::main
"""

import pytest
from ex_packaging_2_cli import main


def test_entry_point_prints_and_returns_success(
    capsys: pytest.CaptureFixture[str],
) -> None:
    assert main(["Ada"]) == 0
    assert capsys.readouterr().out == "Hello, Ada!\n"


def test_missing_argument_reports_usage(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as error:
        main([])
    assert error.value.code == 2
    assert "usage:" in capsys.readouterr().err
