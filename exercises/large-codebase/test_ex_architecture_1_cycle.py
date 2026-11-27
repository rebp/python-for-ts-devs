"""Tests for exercise 13.2-1.

Edit: ex_architecture_1_shop/models.py
"""

import os
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.parametrize("first", ["pricing", "inventory"])
def test_imports_in_either_order_and_shares_the_model(
    first: str, lesson_dir: Path, tmp_path: Path
) -> None:
    code = f"""
import importlib
importlib.import_module("ex_architecture_1_shop.{first}")
from ex_architecture_1_shop import inventory, models, pricing
assert inventory.Product is pricing.Product is models.Product
product = models.Product("pen", 150)
assert pricing.total([product, product]) == 300
assert inventory.inventory_value([product]) == 150
"""
    result = subprocess.run(
        [sys.executable, "-c", code],
        cwd=tmp_path,
        env={**os.environ, "PYTHONPATH": str(lesson_dir)},
        capture_output=True,
        text=True,
        timeout=20,
        check=False,
    )
    assert result.returncode == 0, result.stderr
