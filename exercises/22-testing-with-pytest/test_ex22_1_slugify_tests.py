"""Tests for exercise 22-1 (Testing with pytest).

Edit: ex22_1_slugify_tests.py::
"""

import ast
import re

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex22_1_slugify_tests.py"

BROKEN = {
    "forgets to lowercase": """
def slugify(text):
    cleaned = "".join(ch for ch in text if ch.isalnum() or ch.isspace())
    return "-".join(cleaned.split())
""",
    "keeps punctuation": """
def slugify(text):
    return "-".join(text.lower().split())
""",
    "drops digits": """
def slugify(text):
    cleaned = "".join(ch for ch in text.lower() if ch.isalpha() or ch.isspace())
    return "-".join(cleaned.split())
""",
    "turns repeated spaces into repeated hyphens": """
def slugify(text):
    cleaned = "".join(ch for ch in text.lower() if ch.isalnum() or ch.isspace())
    return cleaned.strip().replace(" ", "-")
""",
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_uses_parametrize(lesson_dir):
    tree = ast.parse((lesson_dir / LEARNER_FILE).read_text(encoding="utf-8"))
    decorators = [
        d
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        for d in node.decorator_list
    ]
    assert any("parametrize" in ast.unparse(d) for d in decorators), (
        "use @pytest.mark.parametrize"
    )


def test_your_tests_pass_against_the_working_slugify(working_run):
    passed, output = working_run
    assert passed, "your tests fail against the working slugify:\n" + output
    match = re.search(r"(\d+) passed", output)
    assert match and int(match.group(1)) >= 3, "write at least three test cases"


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_slugify(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against the working slugify"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path, lesson_dir, {"slugify": BROKEN[bug]}
    )
    assert not passed, (
        f"your tests still pass when slugify {bug}. Add a case that catches it."
    )
