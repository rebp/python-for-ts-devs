"""Tests for exercise 13.3-2.

Edit: ex_modern_2_annotations.py::unresolved_annotations
"""

from ex_modern_2_annotations import unresolved_annotations


def test_finds_unresolved_names_without_requiring_them_to_exist() -> None:
    namespace: dict[str, object] = {}
    exec(  # noqa: S102
        "def example(item: MissingType, count: int) -> MissingReturn: return count",
        namespace,
    )
    function = namespace["example"]
    assert callable(function)
    assert unresolved_annotations(function) == ["item"]


def test_resolved_annotations_are_not_reported() -> None:
    def example(value: int) -> str:
        return str(value)

    assert unresolved_annotations(example) == []
