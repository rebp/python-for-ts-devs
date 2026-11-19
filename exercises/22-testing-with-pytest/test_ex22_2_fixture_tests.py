"""Tests for exercise 22-2 (Testing with pytest).

Edit: ex22_2_fixture_tests.py::
"""

import ast
import re

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex22_2_fixture_tests.py"

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
OK_DEPOSIT = "self._balance += amount"
OK_WITHDRAW = "self._balance -= amount"

BROKEN = {
    "deposit doesn't change the balance": TEMPLATE.replace("DEPOSIT", "pass").replace(
        "WITHDRAW", OK_WITHDRAW
    ),
    "withdraw adds instead of subtracting": TEMPLATE.replace(
        "DEPOSIT", OK_DEPOSIT
    ).replace("WITHDRAW", OK_DEPOSIT),
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_has_an_account_fixture_used_by_two_tests(lesson_dir):
    tree = ast.parse((lesson_dir / LEARNER_FILE).read_text(encoding="utf-8"))
    functions = [node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    fixture = [
        f
        for f in functions
        if f.name == "account"
        and any("fixture" in ast.unparse(d) for d in f.decorator_list)
    ]
    assert fixture, "define a fixture: @pytest.fixture def account(): ..."
    users = [
        f
        for f in functions
        if f.name.startswith("test") and "account" in [a.arg for a in f.args.args]
    ]
    assert len(users) >= 2, (
        "write at least two tests that take `account` as a parameter"
    )


def test_your_tests_pass_against_the_working_account(working_run):
    passed, output = working_run
    assert passed, "your tests fail against the working Account:\n" + output
    match = re.search(r"(\d+) passed", output)
    assert match and int(match.group(1)) >= 2, "write at least two tests"


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_account(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against the working Account"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path, lesson_dir, {"bank": BROKEN[bug]}
    )
    assert not passed, f"your tests still pass when {bug}."
