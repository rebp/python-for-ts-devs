"""Tests for exercise 06-3 (Mutable and immutable).

Edit: ex06_3_dict_keys.py::try_as_key
"""

import pytest
from ex06_3_dict_keys import try_as_key


@pytest.mark.parametrize("key", [(1, 2), "text", 42, None])
def test_immutable_keys_work(key):
    assert try_as_key(key) == "ok"


@pytest.mark.parametrize("key", [[1, 2], {"a": 1}, {1, 2}])
def test_mutable_keys_fail(key):
    assert try_as_key(key) == "TypeError"


def test_a_tuple_holding_a_list_fails_too():
    assert try_as_key((1, [2])) == "TypeError"
