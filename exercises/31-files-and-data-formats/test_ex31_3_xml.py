"""Tests for exercise 31-3 (Files and data formats).

Edit: ex31_3_xml.py::book_years
"""

from ex31_3_xml import book_years

XML = '<books><book year="1965"><title>Dune</title></book><book year="1969"><title>Ubik</title></book></books>'


def test_course_example():
    assert book_years(XML) == [("Dune", 1965), ("Ubik", 1969)]


def test_no_books():
    assert book_years("<books></books>") == []
