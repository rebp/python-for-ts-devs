"""Reference solution for exercise 9.2-2."""

from pathlib import Path

from lxml import etree


def count_sections(path: Path) -> int:
    """Count sections while releasing processed elements."""
    count = 0
    for _, element in etree.iterparse(
        str(path),
        events=("end",),
        tag="{urn:example:sts}sec",
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
    ):
        count += 1
        parent = element.getparent()
        element.clear()
        if parent is not None:
            while element.getprevious() is not None:
                del parent[0]
    return count
