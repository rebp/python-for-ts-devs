"""Tests for exercise 03-3 (Functions).

Edit: ex03_3_make_tag.py::make_tag
"""

from ex03_3_make_tag import make_tag


def test_link():
    assert make_tag("a", "Home", href="/") == '<a href="/">Home</a>'


def test_no_attributes():
    assert make_tag("p", "Hi") == "<p>Hi</p>"


def test_several_attributes_keep_their_order():
    result = make_tag("a", "Docs", href="/docs", target="_blank")
    assert result == '<a href="/docs" target="_blank">Docs</a>'


def test_attributes_from_a_dict():
    attrs = {"class": "btn", "id": "save"}
    assert (
        make_tag("button", "Save", **attrs)
        == '<button class="btn" id="save">Save</button>'
    )
