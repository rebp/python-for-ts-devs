"""Tests for exercise 22-3 (Testing with pytest).

Edit: ex22_3_raises_tests.py::
"""

import ast

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex22_3_raises_tests.py"

TEMPLATE = """
class Account:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0.0

    def deposit(self, amount):
        DEPOSIT

    def withdraw(self, amount):
        WITHDRAW

    @property
    def total(self):
        return self._balance
"""
DEPOSIT = "self._balance += amount"


def withdraw_raising(statement):
    return f"if amount > self._balance:\n            {statement}\n        self._balance -= amount"


BROKEN = {
    "withdraw allows an overdraft": TEMPLATE.replace("DEPOSIT", DEPOSIT).replace(
        "WITHDRAW", "self._balance -= amount"
    ),
    "withdraw raises RuntimeError instead of ValueError": TEMPLATE.replace(
        "DEPOSIT", DEPOSIT
    ).replace("WITHDRAW", withdraw_raising('raise RuntimeError("insufficient funds")')),
    "the error message doesn't mention insufficient funds": TEMPLATE.replace(
        "DEPOSIT", DEPOSIT
    ).replace("WITHDRAW", withdraw_raising('raise ValueError("nope")')),
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_uses_pytest_raises_with_match(lesson_dir):
    tree = ast.parse((lesson_dir / LEARNER_FILE).read_text(encoding="utf-8"))
    calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and ast.unparse(node.func).endswith("raises")
    ]
    assert calls, "use with pytest.raises(...)"
    assert any(kw.arg == "match" for call in calls for kw in call.keywords), (
        "pass match= to check the message"
    )


def test_your_tests_pass_against_the_working_account(working_run):
    passed, output = working_run
    assert passed, "your tests fail against the working Account:\n" + output


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_account(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against the working Account"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path, lesson_dir, {"bank": BROKEN[bug]}
    )
    assert not passed, f"your tests still pass when {bug}."
