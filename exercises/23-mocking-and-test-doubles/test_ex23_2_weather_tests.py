"""Tests for exercise 23-2 (Mocking and test doubles).

Edit: ex23_2_weather_tests.py::
"""

import re

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex23_2_weather_tests.py"

BROKEN = {
    "treats 20°C as cold": """
from ex23_weather_api import fetch_temperature

def describe(city):
    temperature = fetch_temperature(city)
    feel = "warm" if temperature > 20 else "cold"
    return f"{city}: {temperature:.0f}°C, {feel}"
""",
    "doesn't round the temperature": """
from ex23_weather_api import fetch_temperature

def describe(city):
    temperature = fetch_temperature(city)
    feel = "warm" if temperature >= 20 else "cold"
    return f"{city}: {temperature}°C, {feel}"
""",
    "asks for the wrong city": """
from ex23_weather_api import fetch_temperature

def describe(city):
    temperature = fetch_temperature(city.lower())
    feel = "warm" if temperature >= 20 else "cold"
    return f"{city}: {temperature:.0f}°C, {feel}"
""",
    "always says warm": """
from ex23_weather_api import fetch_temperature

def describe(city):
    temperature = fetch_temperature(city)
    return f"{city}: {temperature:.0f}°C, warm"
""",
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_uses_patch(lesson_dir):
    source = (lesson_dir / LEARNER_FILE).read_text(encoding="utf-8")
    assert re.search(r"\bpatch\(|monkeypatch\.setattr\(", source), (
        "replace fetch_temperature with patch(...) or monkeypatch.setattr(...)"
    )


def test_your_tests_pass_against_the_working_describe(working_run):
    passed, output = working_run
    assert passed, (
        "your tests fail against the working describe. If you see 'needs the "
        "network', you patched the wrong name: patch "
        "ex23_weather_report.fetch_temperature.\n" + output
    )
    match = re.search(r"(\d+) passed", output)
    assert match and int(match.group(1)) >= 3, "write at least three tests"


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_describe(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against the working describe"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE,
        tmp_path,
        lesson_dir,
        {"ex23_weather_report": BROKEN[bug]},
    )
    assert not passed, (
        f"your tests still pass when describe {bug}. Add a test that catches it."
    )
