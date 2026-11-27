"""Tests for exercise 11.2-2.

Edit: ex_ci_2_clean.py::mean
"""

import subprocess
import sys
from pathlib import Path

import pytest
from ex_ci_2_clean import mean


def test_mean_and_empty_input() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0
    with pytest.raises(ValueError):
        mean([])


def test_ruff_and_mypy_pass(lesson_dir: Path, tmp_path: Path) -> None:
    path = lesson_dir / "ex_ci_2_clean.py"
    commands = [
        [sys.executable, "-m", "ruff", "check", str(path)],
        [
            sys.executable,
            "-m",
            "mypy",
            "--strict",
            "--cache-dir",
            str(tmp_path / "cache"),
            str(path),
        ],
    ]
    for command in commands:
        result = subprocess.run(
            command,
            cwd=tmp_path,
            capture_output=True,
            text=True,
            timeout=60,
            check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
