"""Reference solution for exercise 3.7-2."""

from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class CaseKey:
    """A case-insensitive, immutable key."""

    name: str

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CaseKey):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()

    def __hash__(self) -> int:
        return hash(self.name.casefold())
