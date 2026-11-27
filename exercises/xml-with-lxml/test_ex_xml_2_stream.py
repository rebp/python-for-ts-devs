"""Tests for exercise 9.2-2.

Edit: ex_xml_2_stream.py::count_sections
"""

from pathlib import Path

import pytest
from ex_xml_2_stream import count_sections
from lxml import etree

from course_helpers import calls_name


def test_stream_a_generated_file(tmp_path: Path) -> None:
    path = tmp_path / "standard.xml"
    with path.open("wb") as file:
        file.write(b'<standard xmlns="urn:example:sts"><body>')
        for _ in range(5000):
            file.write(b"<sec><title>Scope</title><p>Text</p></sec>")
        file.write(b"</body></standard>")
    assert count_sections(path) == 5000


def test_only_the_requested_namespace_is_counted(tmp_path: Path) -> None:
    path = tmp_path / "standard.xml"
    path.write_bytes(b'<standard xmlns="urn:other"><sec/></standard>')
    assert count_sections(path) == 0


def test_bad_xml_is_reported(tmp_path: Path) -> None:
    path = tmp_path / "broken.xml"
    path.write_bytes(b'<standard xmlns="urn:example:sts"><sec/>')
    with pytest.raises(etree.XMLSyntaxError):
        count_sections(path)


def test_processes_and_clears_elements_incrementally() -> None:
    assert calls_name(count_sections, "iterparse")
    assert calls_name(count_sections, "clear")
