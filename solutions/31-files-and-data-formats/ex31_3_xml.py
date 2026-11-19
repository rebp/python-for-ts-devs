"""Reference solution for exercise 31-3 (Files and data formats)."""

import xml.etree.ElementTree as ET


def book_years(xml_text: str) -> list[tuple[str, int]]:
    """Parse this XML and print each title with its year:
    <books><book year="1965"><title>Dune</title></book><book year="1969"><title>Ubik</title></book></books>

    book_years(xml_text) returns the (title, year) pairs instead of printing
    them, with the year as an int: [("Dune", 1965), ("Ubik", 1969)].
    Use xml.etree.ElementTree.
    """
    root = ET.fromstring(xml_text)
    return [
        (book.findtext("title"), int(book.get("year"))) for book in root.findall("book")
    ]
