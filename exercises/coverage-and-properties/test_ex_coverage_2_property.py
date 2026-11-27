"""Tests for exercise 6.3-2.

Edit: ex_coverage_2_property.py::test_words
"""

from pathlib import Path

from ex_coverage_2_property import test_words as learner_property
from hypothesis import is_hypothesis_test

from course_helpers import run_learner_tests

BROKEN = """
def normalize(text: str) -> str:
    return text.replace(" ", "")
"""


def test_property_uses_hypothesis() -> None:
    assert is_hypothesis_test(learner_property)


def test_property_passes_for_correct_code(lesson_dir: Path, tmp_path: Path) -> None:
    passed, output = run_learner_tests(
        lesson_dir / "ex_coverage_2_property.py", tmp_path, lesson_dir
    )
    assert passed, output


def test_property_catches_the_bug(lesson_dir: Path, tmp_path: Path) -> None:
    passed, output = run_learner_tests(
        lesson_dir / "ex_coverage_2_property.py",
        tmp_path,
        lesson_dir,
        replacements={"ex_coverage_words": BROKEN},
    )
    assert not passed and "AssertionError" in output, output
