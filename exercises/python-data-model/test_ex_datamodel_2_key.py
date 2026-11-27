"""Tests for exercise 3.7-2.

Edit: ex_datamodel_2_key.py::CaseKey
"""

from dataclasses import FrozenInstanceError

import pytest
from ex_datamodel_2_key import CaseKey


def test_equal_keys_have_equal_hashes_and_work_in_sets() -> None:
    first, second = CaseKey("Ada"), CaseKey("ADA")
    assert first == second
    assert hash(first) == hash(second)
    assert second in {first}
    assert CaseKey("Grace") != first
    assert first != "Ada"


def test_key_cannot_change_after_hashing() -> None:
    key = CaseKey("Ada")
    with pytest.raises(FrozenInstanceError):
        key.name = "Grace"  # type: ignore[misc]
