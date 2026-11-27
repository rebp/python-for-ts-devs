"""Checks for curriculum ordering and backwards-compatible exercise IDs."""

import json
import re
from html.parser import HTMLParser
from pathlib import Path

import pytest

import course


@pytest.fixture
def concurrent_exercises(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> list[course.Exercise]:
    for folder, filename in (
        ("29-async", "test_ex29_1_basic.py"),
        ("30-threads", "test_ex30_1_threads.py"),
        ("async-production", "test_ex_asyncprod_1_workers.py"),
    ):
        directory = tmp_path / folder
        directory.mkdir()
        (directory / filename).touch()
    monkeypatch.setattr(course, "EXERCISES", tmp_path)
    return course.discover()


def test_discovery_uses_topic_order_not_folder_order(
    concurrent_exercises: list[course.Exercise],
) -> None:
    assert [item.id for item in concurrent_exercises] == [
        "29-1",
        "asyncprod-1",
        "30-1",
    ]
    assert [item.display_id for item in concurrent_exercises] == [
        "8.1-1",
        "8.2-1",
        "8.3-1",
    ]


def test_new_and_legacy_selectors_choose_the_same_exercise(
    concurrent_exercises: list[course.Exercise], monkeypatch: pytest.MonkeyPatch
) -> None:
    checked: list[str] = []

    def record(exercise: course.Exercise, *_args: object) -> int:
        checked.append(exercise.id)
        return 0

    monkeypatch.setattr(course, "check", record)
    assert course.cmd_one("29-1", concurrent_exercises, {}) == 0
    assert course.cmd_one("8.1-1", concurrent_exercises, {}) == 0
    assert course.cmd_one("8.2-1", concurrent_exercises, {}) == 0
    assert checked == ["29-1", "29-1", "asyncprod-1"]


def test_existing_progress_keeps_its_stable_ids(
    concurrent_exercises: list[course.Exercise],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    progress_file = tmp_path / "progress.json"
    progress_file.write_text(
        json.dumps({"completed": {"29-1": "2026-01-01"}}), encoding="utf-8"
    )
    monkeypatch.setattr(course, "PROGRESS_FILE", progress_file)
    completed = course.load_progress()
    next_item = course.next_exercise(concurrent_exercises, completed)
    assert next_item is not None
    assert next_item is concurrent_exercises[1]
    course.mark_done(next_item, completed)
    assert set(course.load_progress()) == {"29-1", "asyncprod-1"}


def test_site_and_runner_use_the_same_curriculum_and_exercises() -> None:
    class CoursePage(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.lessons: dict[str, int] = {}
            self.tasks: dict[str, bool] = {}

        def handle_starttag(
            self, tag: str, attrs: list[tuple[str, str | None]]
        ) -> None:
            values = dict(attrs)
            classes = (values.get("class") or "").split()
            if tag == "template" and "lesson" in classes:
                lesson, section = values.get("data-n"), values.get("data-section")
                assert lesson and section and lesson not in self.lessons
                self.lessons[lesson] = int(section)
            if tag == "li" and "task" in classes:
                task = values.get("data-task")
                assert task and task not in self.tasks
                self.tasks[task] = "data-manual" in values

    html = (course.ROOT / "index.html").read_text(encoding="utf-8")
    page = CoursePage()
    page.feed(html)
    entries = re.findall(
        r"^\s*(\d+): \{ name: .* ids: (\[.*\]) \},?$", html, re.MULTILINE
    )
    site_sections = {int(section): json.loads(ids) for section, ids in entries}
    assert site_sections == {
        section: list(ids) for section, (_, ids) in course.SECTIONS.items()
    }

    exercises = course.discover()
    assert page.lessons == {item.lesson: item.section for item in exercises}
    assert page.tasks == {item.id: item.manual for item in exercises}
