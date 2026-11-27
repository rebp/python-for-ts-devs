"""Reference solution for exercise 9.2-1."""

from lxml import etree


def section_titles(xml: bytes) -> list[str]:
    """Return the text of every section title without resolving entities."""
    parser = etree.XMLParser(resolve_entities=False, no_network=True, load_dtd=False)
    root = etree.fromstring(xml, parser)
    titles = root.xpath("//s:sec/s:title", namespaces={"s": "urn:example:sts"})
    return ["".join(title.itertext()) for title in titles]
