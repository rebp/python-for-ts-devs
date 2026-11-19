"""Shared pytest setup for the exercise pack.

The tests live in exercises/ and import your code by module name
(for example `from ex03_2_average import average`).

`pytest --solutions` runs the same tests against the reference solutions:
an import hook makes every exercise module resolve to its twin in solutions/.
"""

import importlib.abc
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent
EXERCISES = ROOT / "exercises"
SOLUTIONS = ROOT / "solutions"

# Lets the tests `import course_helpers` from any lesson folder.
sys.path.insert(0, str(ROOT))


class _SolutionsFinder(importlib.abc.MetaPathFinder):
    """Resolves top-level exercise modules and packages to files in solutions/."""

    def __init__(self, solutions: Path) -> None:
        self.index: dict[str, Path] = {}
        for lesson in sorted(solutions.iterdir()):
            if not lesson.is_dir():
                continue
            for entry in lesson.iterdir():
                if entry.suffix == ".py" and not entry.name.startswith("test_"):
                    self.index[entry.stem] = entry
                elif entry.is_dir() and (entry / "__init__.py").exists():
                    self.index[entry.name] = entry

    def find_spec(self, name, path=None, target=None):
        if path is not None or name not in self.index:
            return None
        location = self.index[name]
        if location.is_dir():
            return importlib.util.spec_from_file_location(
                name,
                location / "__init__.py",
                submodule_search_locations=[str(location)],
            )
        return importlib.util.spec_from_file_location(name, location)


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--solutions",
        action="store_true",
        help="run the exercise tests against the reference solutions in solutions/",
    )


def pytest_configure(config: pytest.Config) -> None:
    if config.getoption("solutions"):
        sys.meta_path.insert(0, _SolutionsFinder(SOLUTIONS))


@pytest.fixture(scope="module")
def lesson_dir(request: pytest.FixtureRequest) -> Path:
    """The folder that holds the code under test: exercises/<lesson> or solutions/<lesson>."""
    lesson = request.path.parent.name
    base = SOLUTIONS if request.config.getoption("solutions") else EXERCISES
    return base / lesson
