"""Tests for exercise 23-1 (Mocking and test doubles).

Edit: ex23_1_checkout_tests.py::
"""

import re

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex23_1_checkout_tests.py"

HEADER = """
class PaymentDeclined(Exception):
    pass


class PaymentGateway:
    def charge(self, amount_cents):
        raise RuntimeError("no network")
"""

BROKEN = {
    "charges euros instead of cents": HEADER
    + """
def checkout(total, gateway):
    try:
        transaction_id = gateway.charge(total)
    except PaymentDeclined:
        return "declined"
    return f"paid {transaction_id}"
""",
    "charges the card twice": HEADER
    + """
def checkout(total, gateway):
    try:
        gateway.charge(round(total * 100))
        transaction_id = gateway.charge(round(total * 100))
    except PaymentDeclined:
        return "declined"
    return f"paid {transaction_id}"
""",
    "lets PaymentDeclined escape": HEADER
    + """
def checkout(total, gateway):
    transaction_id = gateway.charge(round(total * 100))
    return f"paid {transaction_id}"
""",
    "ignores the transaction id": HEADER
    + """
def checkout(total, gateway):
    try:
        gateway.charge(round(total * 100))
    except PaymentDeclined:
        return "declined"
    return "paid"
""",
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_uses_a_mock(lesson_dir):
    source = (lesson_dir / LEARNER_FILE).read_text(encoding="utf-8")
    assert re.search(r"\b(Mock|MagicMock|create_autospec)\(", source), (
        "replace the gateway with a Mock(), MagicMock() or create_autospec(...)"
    )


def test_your_tests_pass_against_the_working_checkout(working_run):
    passed, output = working_run
    assert passed, "your tests fail against the working checkout:\n" + output
    match = re.search(r"(\d+) passed", output)
    assert match and int(match.group(1)) >= 2, "write at least two tests"


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_checkout(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against the working checkout"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path, lesson_dir, {"ex23_checkout": BROKEN[bug]}
    )
    assert not passed, (
        f"your tests still pass when checkout {bug}. Add an assertion that catches it."
    )
