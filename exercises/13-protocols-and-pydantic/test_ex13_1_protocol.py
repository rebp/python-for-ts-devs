"""Tests for exercise 13-1 (Protocols and Pydantic).

Edit: ex13_1_protocol.py::total_size
"""

from typing import Protocol

from ex13_1_protocol import Folder, Photo, Sized, total_size


def test_sized_is_a_protocol_with_size():
    assert Protocol in Sized.__mro__
    assert callable(getattr(Sized, "size", None)), "declare def size(self) -> int: ..."


def test_classes_do_not_inherit_from_sized():
    assert Sized not in Folder.__mro__
    assert Sized not in Photo.__mro__


def test_classes_have_int_sizes():
    assert isinstance(Folder().size(), int)
    assert isinstance(Photo().size(), int)


def test_total_size():
    assert total_size([Folder(), Photo()]) == Folder().size() + Photo().size()
    assert total_size([]) == 0


def test_works_with_any_object_that_has_size():
    class Box:
        def size(self) -> int:
            return 7

    assert total_size([Box(), Box()]) == 14
