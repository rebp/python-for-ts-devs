"""Tests for exercise 9.2-1.

Edit: ex_xml_1_titles.py::section_titles
"""

from pathlib import Path

import pytest
from ex_xml_1_titles import section_titles
from lxml import etree


def test_namespaces_and_mixed_text() -> None:
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
    <standard xmlns="urn:example:sts"><body>
      <sec><title>Use <italic>safe</italic> parsing</title></sec>
      <sec><title>References</title></sec>
    </body></standard>"""
    assert section_titles(xml) == ["Use safe parsing", "References"]


def test_empty_document_and_different_namespace() -> None:
    xml = b'<standard xmlns="urn:example:sts"><sec xmlns="urn:other"><title>Skip</title></sec></standard>'
    assert section_titles(xml) == []


def test_external_entity_cannot_read_a_local_file(tmp_path: Path) -> None:
    secret = tmp_path / "secret.txt"
    secret.write_text("PRIVATE", encoding="utf-8")
    xml = f"""<!DOCTYPE standard [<!ENTITY xxe SYSTEM "{secret.as_uri()}">]>
    <standard xmlns="urn:example:sts"><sec><title>Before &xxe; after</title></sec></standard>
    """.encode()
    assert "PRIVATE" not in "".join(section_titles(xml))


def test_malformed_xml_is_reported() -> None:
    with pytest.raises(etree.XMLSyntaxError):
        section_titles(b"<standard>")
