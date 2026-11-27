"""Tests for exercise 11.3-1.

Edit: ex_packaging_1_metadata.py::read_metadata
"""

import pytest
from ex_packaging_1_metadata import read_metadata


def test_reads_project_and_console_script() -> None:
    text = """
    [project]
    name = "greeter"
    version = "1.2.0"
    [project.scripts]
    greet = "greeter.cli:main"
    """
    assert read_metadata(text) == ("greeter", "1.2.0", {"greet": "greeter.cli:main"})
    assert read_metadata('[project]\nname = "x"\nversion = "1"\n') == ("x", "1", {})


@pytest.mark.parametrize(
    "text",
    [
        "",
        '[project]\nname = ""\nversion = "1"\n',
        '[project]\nname = "x"\nversion = 1\n',
        '[project]\nname = "x"\nversion = "1"\nscripts = { greet = 2 }\n',
    ],
)
def test_rejects_invalid_metadata(text: str) -> None:
    with pytest.raises(ValueError):
        read_metadata(text)
