"""Tests for exercise 10-2 (Dataclasses).

Edit: ex10_2_version.py::sort_versions
"""

from ex10_2_version import Version, sort_versions


def test_versions_compare_field_by_field():
    assert Version(1, 2, 3) < Version(1, 10, 0), "1.10.0 is newer than 1.2.3"
    assert Version(0, 9, 9) < Version(1, 0, 0)


def test_sort_versions():
    versions = [Version(1, 10, 0), Version(1, 2, 3), Version(0, 9, 9)]
    assert sort_versions(versions) == [
        Version(0, 9, 9),
        Version(1, 2, 3),
        Version(1, 10, 0),
    ]


def test_input_is_not_changed():
    versions = [Version(2, 0, 0), Version(1, 0, 0)]
    sort_versions(versions)
    assert versions == [Version(2, 0, 0), Version(1, 0, 0)]
