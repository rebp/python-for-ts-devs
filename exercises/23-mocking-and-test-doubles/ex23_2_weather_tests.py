"""Lesson 23 · Mocking and test doubles · exercise 2.

Test describe() from ex23_weather_report.py. It calls fetch_temperature, which
would need the network, so replace it with unittest.mock.patch.

The catch: ex23_weather_report.py does `from ex23_weather_api import
fetch_temperature`, so it has its own copy of the name. Patch it where it's
looked up, "ex23_weather_report.fetch_temperature", not where it's defined.

Write at least three tests:

- a warm day: with the temperature patched to 23.6, describe("Lisbon") returns
  "Lisbon: 24°C, warm" (the temperature is rounded), and fetch_temperature was
  called once with "Lisbon";
- a cold day, for example 8.0;
- exactly 20°C, which counts as warm.

Use patch as a context manager or a decorator. monkeypatch.setattr
works too.

How it's checked: your tests must pass against ex23_weather_report.py, and fail
against broken versions of it. Run them yourself with:

    uv run pytest exercises/23-mocking-and-test-doubles/ex23_2_weather_tests.py

Check your work with: uv run course.py
"""

from unittest.mock import patch  # noqa: F401  (delete this comment once you use patch)

import pytest
from ex23_weather_report import describe  # noqa: F401


def test_placeholder():
    pytest.fail("Replace this placeholder with your tests")
