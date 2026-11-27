"""Reference solution for exercise 11.2-1."""

from collections.abc import Iterable


def select_versions(versions: Iterable[str], minimum: str) -> list[str]:
    """Compare major and minor components numerically."""

    def components(version: str) -> tuple[int, int]:
        major, separator, minor = version.partition(".")
        if not separator or not major.isdecimal() or not minor.isdecimal():
            raise ValueError(f"invalid Python version: {version}")
        return int(major), int(minor)

    floor = components(minimum)
    return [version for version in versions if components(version) >= floor]
