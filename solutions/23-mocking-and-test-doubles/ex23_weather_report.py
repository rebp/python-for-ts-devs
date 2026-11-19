"""The code that exercise 23-2 tests. You don't need to change it."""

from ex23_weather_api import fetch_temperature


def describe(city: str) -> str:
    """Describe the weather, like "Lisbon: 24°C, warm".

    The temperature is rounded to whole degrees, and 20°C or more is warm.
    """
    temperature = fetch_temperature(city)
    feel = "warm" if temperature >= 20 else "cold"
    return f"{city}: {temperature:.0f}°C, {feel}"
