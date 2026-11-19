"""Tests for exercise 19-2 (Modules and imports).

Edit: shop/pricing.py::demo
"""

import subprocess
import sys


def run(lesson_dir, *args):
    result = subprocess.run(
        [sys.executable, *args],
        cwd=lesson_dir,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def test_running_the_module_prints_the_demo(lesson_dir):
    assert run(lesson_dir, "-m", "shop.pricing").strip() == "demo: 90.0"


def test_importing_the_module_prints_nothing(lesson_dir):
    assert run(lesson_dir, "-c", "import shop.pricing") == ""


def test_main_does_not_print_the_demo(lesson_dir):
    assert "demo" not in run(lesson_dir, "main.py")
