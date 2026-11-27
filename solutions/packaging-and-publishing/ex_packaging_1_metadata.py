"""Reference solution for exercise 11.3-1."""

import tomllib


def read_metadata(text: str) -> tuple[str, str, dict[str, str]]:
    """Read the required metadata and optional console scripts."""
    data = tomllib.loads(text)
    project = data.get("project")
    if not isinstance(project, dict):
        raise ValueError("project table is required")  # noqa: TRY004
    name, version = project.get("name"), project.get("version")
    scripts = project.get("scripts", {})
    if (
        not isinstance(name, str)
        or not name
        or not isinstance(version, str)
        or not version
    ):
        raise ValueError("name and version must be nonempty strings")
    if not isinstance(scripts, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in scripts.items()
    ):
        raise ValueError("scripts must map strings to strings")
    return name, version, scripts
