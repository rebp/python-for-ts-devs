"""Tests for exercise 3.7-1.

Edit: ex_datamodel_1_playlist.py::Playlist
"""

import pytest
from ex_datamodel_1_playlist import Playlist


def test_sequence_operations_and_copy_of_input() -> None:
    songs = ["one", "two"]
    playlist = Playlist(songs)
    songs.append("later")
    assert len(playlist) == 2
    assert list(playlist) == ["one", "two"]
    assert playlist[-1] == "two"
    assert "one" in playlist
    assert "missing" not in playlist
    with pytest.raises(IndexError):
        _ = playlist[2]


def test_addition_creates_a_new_playlist() -> None:
    left = Playlist(["a"])
    right = Playlist(["b"])
    combined = left + right
    assert isinstance(combined, Playlist)
    assert list(combined) == ["a", "b"]
    assert list(left) == ["a"]
    assert repr(combined) == "Playlist(['a', 'b'])"
    with pytest.raises(TypeError):
        _ = left + ["not a playlist"]  # type: ignore[operator]
