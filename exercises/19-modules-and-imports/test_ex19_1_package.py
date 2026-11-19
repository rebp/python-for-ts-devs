"""Tests for exercise 19-1 (Modules and imports).

Edit: shop/pricing.py::apply_discount
"""

import subprocess
import sys

from shop.pricing import apply_discount


def test_apply_discount():
    assert apply_discount(80, 25) == 60.0
    assert apply_discount(100, 0) == 100


def test_rounds_to_two_decimals():
    assert apply_discount(19.99, 10) == 17.99


def test_main_prints_the_discounted_price(lesson_dir):
    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=lesson_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() == "60.0"
