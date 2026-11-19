"""Reference solution for exercise 23-2 (Mocking and test doubles)."""

from unittest.mock import patch

from ex23_weather_report import describe

# Patch the name where describe() looks it up, not where it's defined.
TARGET = "ex23_weather_report.fetch_temperature"


def test_warm_day():
    with patch(TARGET, return_value=23.6) as fake_fetch:
        assert describe("Lisbon") == "Lisbon: 24°C, warm"
    fake_fetch.assert_called_once_with("Lisbon")


@patch(TARGET, return_value=8.0)
def test_cold_day(fake_fetch):
    assert describe("Oslo") == "Oslo: 8°C, cold"


def test_twenty_degrees_is_warm(monkeypatch):
    monkeypatch.setattr(TARGET, lambda city: 20.0)
    assert describe("Rome") == "Rome: 20°C, warm"
