"""Tests for exercise 13.3-1.

Edit: ex_modern_1_template.py::render_html
"""

from ex_modern_1_template import render_html


def test_escapes_values_but_keeps_trusted_literals() -> None:
    name = '<Ada & "Lin">'
    assert render_html(t"<p>{name}</p>") == "<p>&lt;Ada &amp; &quot;Lin&quot;&gt;</p>"


def test_conversion_formatting_and_empty_template() -> None:
    name = "Ada"
    price = 2.5
    assert render_html(t"{name!r}: {price:.1f}") == "&#x27;Ada&#x27;: 2.5"
    assert render_html(t"") == ""
