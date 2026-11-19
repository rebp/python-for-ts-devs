"""Tests for exercise 10-1 (Dataclasses).

Edit: ex10_1_book.py::Book
"""

from dataclasses import fields, is_dataclass

from ex10_1_book import Book


def test_is_a_dataclass_with_the_right_fields():
    assert is_dataclass(Book)
    assert [f.name for f in fields(Book)] == ["title", "author", "year", "tags"]


def test_tags_default_to_empty():
    book = Book("Dune", "Frank Herbert", 1965)
    assert book.tags == []
    assert book.year == 1965


def test_books_do_not_share_tags():
    first = Book("Dune", "Frank Herbert", 1965)
    second = Book("Ubik", "Philip K. Dick", 1969)
    first.tags.append("sci-fi")
    assert second.tags == []


def test_equality_and_repr_come_for_free():
    assert Book("Dune", "Frank Herbert", 1965, ["sf"]) == Book(
        "Dune", "Frank Herbert", 1965, ["sf"]
    )
    assert "Dune" in repr(Book("Dune", "Frank Herbert", 1965))
