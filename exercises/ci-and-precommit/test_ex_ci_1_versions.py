"""Tests for exercise 11.2-1.

Edit: ex_ci_1_versions.py::select_versions
"""

import pytest
from ex_ci_1_versions import select_versions


def test_compares_minor_versions_as_numbers() -> None:
    versions = iter(["3.9", "3.15", "3.10", "4.0"])
    assert select_versions(versions, "3.10") == ["3.15", "3.10", "4.0"]
    assert select_versions(["3.15"], "3.16") == []


@pytest.mark.parametrize(
    "versions, minimum", [(["3.x"], "3.10"), (["3.15"], "3"), (["3.15.1"], "3.10")]
)
def test_rejects_invalid_versions(versions: list[str], minimum: str) -> None:
    with pytest.raises(ValueError):
        select_versions(versions, minimum)
