"""Reference solution for exercise 3.7-1."""

from collections.abc import Iterator


class Playlist:
    """An immutable sequence of song names."""

    def __init__(self, songs: list[str]) -> None:
        self._songs = tuple(songs)

    def __len__(self) -> int:
        return len(self._songs)

    def __iter__(self) -> Iterator[str]:
        return iter(self._songs)

    def __getitem__(self, index: int) -> str:
        return self._songs[index]

    def __contains__(self, song: object) -> bool:
        return song in self._songs

    def __add__(self, other: Playlist) -> Playlist:
        if not isinstance(other, Playlist):
            return NotImplemented
        return Playlist(list(self._songs + other._songs))

    def __repr__(self) -> str:
        return f"Playlist({list(self._songs)!r})"
