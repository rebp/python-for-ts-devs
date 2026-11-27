"""Tests for exercise 12.2-2.

Edit: ex_arrays_2_totals.py::totals_by_category
"""

import polars as pl
import pytest
from ex_arrays_2_totals import totals_by_category


def test_filters_groups_and_sorts_lazily() -> None:
    frame = pl.DataFrame(
        {"category": ["b", "a", "a", "b", "c"], "amount": [5, 1, 2, -2, None]}
    ).lazy()
    result = totals_by_category(frame)
    assert isinstance(result, pl.LazyFrame)
    assert result.collect().to_dicts() == [
        {"category": "a", "total": 3},
        {"category": "b", "total": 5},
    ]


def test_missing_column_is_reported() -> None:
    frame = pl.DataFrame({"other": [1]}).lazy()
    with pytest.raises(pl.exceptions.ColumnNotFoundError):
        totals_by_category(frame).collect()
