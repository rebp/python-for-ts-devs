"""Lesson 3.7 · The data model · exercise 1.

Check your work with: uv run course.py 3.7-1
"""

from collections.abc import Iterator


class Playlist:
    """Make a playlist behave like a small immutable sequence of song names."""

    def __init__(self, songs: list[str]) -> None:
        self._songs = tuple(songs)

    def __len__(self) -> int:
        raise NotImplementedError("Your code here")

    def __iter__(self) -> Iterator[str]:
        raise NotImplementedError("Your code here")

    def __getitem__(self, index: int) -> str:
        raise NotImplementedError("Your code here")

    def __contains__(self, song: object) -> bool:
        raise NotImplementedError("Your code here")

    def __add__(self, other: Playlist) -> Playlist:
        raise NotImplementedError("Your code here")

    def __repr__(self) -> str:
        raise NotImplementedError("Your code here")
