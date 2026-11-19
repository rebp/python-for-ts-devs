"""Tests for exercise 38-3 (Command-line tools with Typer).

Edit: ex38_3_count_rows.py::count_rows
"""

import pytest
from ex38_3_count_rows import app
from typer.testing import CliRunner

runner = CliRunner()


@pytest.fixture
def orders(tmp_path):
    path = tmp_path / "orders.csv"
    path.write_text(
        "order_id,region,product\n1,EU,Lamp\n2,US,Desk\n3,EU,Chair\n",
        encoding="utf-8",
    )
    return path


def run(*args):
    return runner.invoke(app, [str(arg) for arg in args])


def test_counts_rows(orders):
    result = run(orders)
    assert result.exit_code == 0, result.output
    assert result.stdout == "3 rows\n"


def test_one_row(tmp_path):
    path = tmp_path / "one.csv"
    path.write_text("name\nAda\n", encoding="utf-8")
    assert run(path).stdout == "1 row\n"


def test_distinct_values_in_a_column(orders):
    result = run(orders, "--column", "region")
    assert result.exit_code == 0, result.output
    assert result.stdout == "2 distinct values in region\n"


def test_unknown_column(orders):
    result = run(orders, "--column", "price")
    assert result.exit_code == 1
    assert "no column named price" in result.stderr


def test_missing_file_is_rejected_by_typer(tmp_path):
    assert run(tmp_path / "missing.csv").exit_code == 2


def test_folder_is_rejected_by_typer(tmp_path):
    assert run(tmp_path).exit_code == 2
