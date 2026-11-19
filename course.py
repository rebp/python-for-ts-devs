"""Exercise runner for "Python for TypeScript developers".

uv run course.py              show the next exercise and check it
uv run course.py 03-2         check one exercise by its id
uv run course.py --done       mark the current README exercise as done
uv run course.py --list       list every exercise and its status
uv run course.py --progress   show your progress per section
uv run course.py --reset      forget your progress
"""

from __future__ import annotations

import sys

if sys.version_info < (3, 12):  # noqa: UP036  (a friendly message for the system Python)
    sys.exit("This course needs Python 3.12 or newer. Run it with: uv run course.py")

import argparse
import ast
import json
import os
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = ROOT / "exercises"
SOLUTIONS = ROOT / "solutions"
PROGRESS_FILE = ROOT / "progress.json"

SECTIONS = {
    1: ("Python for TypeScript developers", range(1, 5)),
    2: ("How Python handles data", range(5, 9)),
    3: ("Your own types", range(9, 15)),
    4: ("Collections and errors", range(15, 19)),
    5: ("Modules, packages and tooling", range(19, 25)),
    6: ("Pythonic Python", range(25, 29)),
    7: ("Beyond the basics", range(29, 35)),
    8: ("Python in the real world", range(35, 41)),
}

LESSONS = {
    1: "Hello, Python",
    2: "Variables and types",
    3: "Functions",
    4: "Control flow",
    5: "Names and objects",
    6: "Mutable and immutable",
    7: "Truthiness, None and equality",
    8: "Scope and the mutable default trap",
    9: "Classes and methods",
    10: "Dataclasses",
    11: "Enums and match",
    12: "Optional values",
    13: "Protocols and Pydantic",
    14: "Typing in depth",
    15: "Lists and tuples",
    16: "Strings in depth",
    17: "Dicts and sets",
    18: "Exceptions",
    19: "Modules and imports",
    20: "Dependencies and environments",
    21: "Linting, formatting and type checking",
    22: "Testing with pytest",
    23: "Mocking and test doubles",
    24: "Debugging",
    25: "Comprehensions and lambdas",
    26: "Iterators and generators",
    27: "Decorators",
    28: "Context managers",
    29: "Async and await",
    30: "Threads, processes and the GIL",
    31: "Files and data formats",
    32: "Dates and times",
    33: "Web APIs with FastAPI",
    34: "Databases",
    35: "Choosing a web framework",
    36: "A real FastAPI service",
    37: "Shipping a web service",
    38: "Command-line tools with Typer",
    39: "Data work with pandas",
    40: "Where to go next",
}

# ---------------------------------------------------------------- terminal output

# Print UTF-8 everywhere. A Windows console already does, but output that's
# redirected to a file or a pipe would otherwise use the legacy code page,
# which can't encode symbols like ✓ and █.
for _stream in (sys.stdout, sys.stderr):
    if (_stream.encoding or "").lower().replace("-", "") != "utf8":
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]


def enable_windows_colors() -> bool:
    """Turn on ANSI color codes in the Windows console. True if it worked."""
    if os.name != "nt":
        return True
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32  # type: ignore[attr-defined]
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
        mode = ctypes.c_uint32()
        if not kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            return False
        return bool(
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        )  # VT processing
    except (AttributeError, OSError):
        return False


COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ and enable_windows_colors()


def paint(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m" if COLOR else text


def bold(text: str) -> str:
    return paint(text, "1")


def dim(text: str) -> str:
    return paint(text, "2")


def green(text: str) -> str:
    return paint(text, "32")


def red(text: str) -> str:
    return paint(text, "31")


def yellow(text: str) -> str:
    return paint(text, "33")


def bar(done: int, total: int, width: int = 24) -> str:
    filled = round(width * done / total) if total else 0
    return green("█" * filled) + dim("░" * (width - filled))


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


# ---------------------------------------------------------------- exercises

TEST_FILE = re.compile(r"test_ex(\d\d)_(\d)_\w+\.py")
README_FILE = re.compile(r"ex(\d\d)_(\d)_\w+\.md")


@dataclass
class Exercise:
    id: str
    lesson: int
    task: int
    path: Path  # the test file, or the README for exercises you check yourself

    @property
    def manual(self) -> bool:
        return self.path.suffix == ".md"

    @property
    def section(self) -> int:
        return next(s for s, (_, lessons) in SECTIONS.items() if self.lesson in lessons)

    @property
    def title(self) -> str:
        return f"Lesson {self.lesson:02d} · {LESSONS[self.lesson]}"


def discover() -> list[Exercise]:
    found = []
    for lesson_dir in sorted(p for p in EXERCISES.iterdir() if p.is_dir()):
        for path in sorted(lesson_dir.iterdir()):
            match = TEST_FILE.fullmatch(path.name) or README_FILE.fullmatch(path.name)
            if match:
                lesson, task = int(match.group(1)), int(match.group(2))
                found.append(Exercise(f"{lesson:02d}-{task}", lesson, task, path))
    return sorted(found, key=lambda e: (e.lesson, e.task))


def edit_target(exercise: Exercise) -> tuple[Path, str]:
    """Which file to edit and which object in it holds the task, from the test's "Edit:" line."""
    doc = ast.get_docstring(ast.parse(exercise.path.read_text(encoding="utf-8"))) or ""
    match = re.search(r"^Edit: (\S+)", doc, re.MULTILINE)
    if not match:
        raise SystemExit(f"{rel(exercise.path)} has no 'Edit:' line in its docstring")
    file_part, _, name = match.group(1).partition("::")
    return exercise.path.parent / file_part, name


def find_docstring(path: Path, dotted_name: str) -> str:
    """The docstring of `Class.method`, `function` or (for an empty name) the module."""
    node: ast.AST = ast.parse(path.read_text(encoding="utf-8"))
    for part in filter(None, dotted_name.split(".")):
        children = getattr(node, "body", [])
        node = next(
            (
                child
                for child in children
                if isinstance(
                    child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
                )
                and child.name == part
            ),
            None,
        )
        if node is None:
            return f"(couldn't find {dotted_name} in {path.name}; did it get renamed?)"
    return ast.get_docstring(node) or "(no docstring)"


def describe(exercise: Exercise, position: int, total: int) -> None:
    print()
    print(bold(f"━━ {exercise.title} " + "━" * max(4, 60 - len(exercise.title))))
    print(f"Exercise {bold(exercise.id)}  {dim(f'({position} of {total})')}")
    if exercise.manual:
        print(f"Instructions: {rel(exercise.path)}")
        print()
        text = exercise.path.read_text(encoding="utf-8")
        text = text.split("This one is checked by you", 1)[0].rstrip()
        print(text)
        return
    target, name = edit_target(exercise)
    label = f"  → {name}" if name else ""
    print(f"File: {bold(rel(target))}{dim(label)}")
    print()
    for line in find_docstring(target, name).splitlines():
        print(f"    {line}" if line else "")


def run_tests(exercise: Exercise, solutions: bool = False) -> tuple[bool, str]:
    command = [
        sys.executable,
        "-m",
        "pytest",
        rel(exercise.path),
        "-q",
        "--tb=short",
        "-p",
        "no:cacheprovider",
    ]
    if solutions:
        command.append("--solutions")
    if COLOR:
        command.append("--color=yes")
    result = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env={**os.environ, "PYTHONUTF8": "1"},  # same output encoding on every OS
        check=False,
    )
    return result.returncode == 0, result.stdout + result.stderr


# ---------------------------------------------------------------- progress


def load_progress() -> dict[str, str]:
    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        return dict(data.get("completed", {}))
    except FileNotFoundError:
        return {}
    except (json.JSONDecodeError, AttributeError):
        sys.exit(
            f"{PROGRESS_FILE.name} is damaged. Fix it by hand or run: uv run course.py --reset"
        )


def save_progress(completed: dict[str, str]) -> None:
    ordered = dict(sorted(completed.items()))
    PROGRESS_FILE.write_text(
        json.dumps({"completed": ordered}, indent=2) + "\n", encoding="utf-8"
    )


def mark_done(exercise: Exercise, completed: dict[str, str]) -> None:
    if exercise.id not in completed:
        completed[exercise.id] = datetime.now().isoformat(timespec="seconds")
        save_progress(completed)


def next_exercise(
    exercises: list[Exercise], completed: dict[str, str]
) -> Exercise | None:
    return next((e for e in exercises if e.id not in completed), None)


# ---------------------------------------------------------------- commands


def show_finished(total: int) -> None:
    print()
    print(green(bold(f"All {total} exercises done. Congratulations!")))
    print(
        "Run any exercise again with: uv run course.py <id>, for example uv run course.py 03-2"
    )


def check(
    exercise: Exercise, exercises: list[Exercise], completed: dict[str, str]
) -> int:
    position = exercises.index(exercise) + 1
    describe(exercise, position, len(exercises))
    print()

    if exercise.manual:
        if exercise.id in completed:
            print(green("✓ You marked this one as done."))
            return 0
        if sys.stdin.isatty():
            answer = input(bold("Done with it? Mark it as complete [y/N] "))
            if answer.strip().lower() in ("y", "yes"):
                mark_done(exercise, completed)
                print(green(f"✓ {exercise.id} done."))
                return after_pass(exercises, completed)
        print(f"When you're done, run: {bold('uv run course.py --done')}")
        return 0

    print(dim("Running the tests…"))
    passed, output = run_tests(exercise)
    if not passed:
        print(output.rstrip())
        print()
        print(
            red(bold(f"✗ {exercise.id} isn't passing yet."))
            + " Edit the file above and run "
            + bold("uv run course.py")
            + " again."
        )
        return 1
    summary = output.strip().splitlines()[-1] if output.strip() else ""
    summary = re.sub(r"\x1b\[[0-9;]*m", "", summary)  # drop pytest's colors
    print(green(bold(f"✓ {exercise.id} passes!")) + dim(f"  {summary}"))
    mark_done(exercise, completed)
    return after_pass(exercises, completed)


def after_pass(exercises: list[Exercise], completed: dict[str, str]) -> int:
    upcoming = next_exercise(exercises, completed)
    if upcoming is None:
        show_finished(len(exercises))
        return 0
    print()
    print(dim("Up next:"))
    describe(upcoming, exercises.index(upcoming) + 1, len(exercises))
    print()
    print(f"When you're ready: {bold('uv run course.py')}")
    return 0


def cmd_next(exercises: list[Exercise], completed: dict[str, str]) -> int:
    current = next_exercise(exercises, completed)
    if current is None:
        show_finished(len(exercises))
        return 0
    return check(current, exercises, completed)


def cmd_one(
    exercise_id: str, exercises: list[Exercise], completed: dict[str, str]
) -> int:
    wanted = exercise_id.strip()
    if re.fullmatch(r"\d-\d", wanted):
        wanted = "0" + wanted
    exercise = next((e for e in exercises if e.id == wanted), None)
    if exercise is None:
        print(
            red(f"No exercise called {exercise_id!r}.")
            + " Ids look like 03-2; see uv run course.py --list"
        )
        return 2
    return check(exercise, exercises, completed)


def cmd_done(exercises: list[Exercise], completed: dict[str, str]) -> int:
    current = next_exercise(exercises, completed)
    if current is None:
        show_finished(len(exercises))
        return 0
    if not current.manual:
        print(
            f"Exercise {current.id} is checked by its tests. Run {bold('uv run course.py')} to check it."
        )
        return 1
    mark_done(current, completed)
    print(green(f"✓ {current.id} marked as done."))
    return after_pass(exercises, completed)


def cmd_list(exercises: list[Exercise], completed: dict[str, str]) -> int:
    current = next_exercise(exercises, completed)
    by_lesson: dict[int, list[Exercise]] = {}
    for exercise in exercises:
        by_lesson.setdefault(exercise.lesson, []).append(exercise)
    for section, (name, lessons) in SECTIONS.items():
        print()
        print(bold(f"{section}. {name}"))
        for lesson in lessons:
            cells = []
            for exercise in by_lesson.get(lesson, []):
                if exercise.id in completed:
                    mark = green("✓")
                elif exercise is current:
                    mark = yellow("▶")
                else:
                    mark = dim("·")
                kind = "*" if exercise.manual else " "
                cells.append(f"{mark} {exercise.id}{dim(kind)}")
            print(f"  {lesson:02d}  {LESSONS[lesson]:<40} {'  '.join(cells)}")
    print()
    print(
        dim("✓ done   ▶ next   · to do   * checked by you (README) instead of by tests")
    )
    return 0


def cmd_progress(exercises: list[Exercise], completed: dict[str, str]) -> int:
    done = sum(1 for e in exercises if e.id in completed)
    total = len(exercises)
    print()
    print(bold("Your progress"))
    print(f"  {bar(done, total)}  {done} / {total} exercises ({done * 100 // total}%)")
    print()
    for section, (name, lessons) in SECTIONS.items():
        in_section = [e for e in exercises if e.lesson in lessons]
        section_done = sum(1 for e in in_section if e.id in completed)
        print(
            f"  {section}. {name:<36} {bar(section_done, len(in_section), 12)}  {section_done}/{len(in_section)}"
        )
    current = next_exercise(exercises, completed)
    print()
    if current is None:
        print(green("Everything is done."))
    else:
        print(
            f"Next up: {bold(current.id)}, {current.title}. Run {bold('uv run course.py')}"
        )
    return 0


def cmd_reset(yes: bool) -> int:
    if not PROGRESS_FILE.exists():
        print("There's no progress to reset.")
        return 0
    if not yes:
        if not sys.stdin.isatty():
            print("Add --yes to confirm: uv run course.py --reset --yes")
            return 1
        answer = input(
            "Forget all your progress? Your code in exercises/ is not touched. [y/N] "
        )
        if answer.strip().lower() not in ("y", "yes"):
            print("Nothing changed.")
            return 0
    PROGRESS_FILE.unlink()
    print("Progress reset. Your code in exercises/ is unchanged.")
    return 0


def cmd_verify(exercises: list[Exercise]) -> int:
    """For course maintainers: tests fail on the stubs in exercises/ and pass on solutions/."""
    problems = []
    for exercise in exercises:
        if exercise.manual:
            answer = SOLUTIONS / exercise.path.parent.name / exercise.path.name
            ok = answer.exists()
            if not ok:
                problems.append(f"{exercise.id}: missing {rel(answer)}")
            print(f"{exercise.id}  README  answer {'ok' if ok else red('missing')}")
            continue
        stub_passes, _ = run_tests(exercise)
        solution_passes, output = run_tests(exercise, solutions=True)
        if stub_passes:
            problems.append(
                f"{exercise.id}: the tests pass against exercises/ (expected them to fail)"
            )
        if not solution_passes:
            problems.append(
                f"{exercise.id}: the tests fail against solutions/\n{output}"
            )
        stub_text = green("fails") if not stub_passes else red("PASSES")
        solution_text = green("passes") if solution_passes else red("FAILS")
        print(f"{exercise.id}  tests  stub {stub_text}  solution {solution_text}")
    print()
    if problems:
        print(red(bold(f"{len(problems)} problem(s):")))
        for problem in problems:
            print(f"- {problem}")
        return 1
    automatic = sum(1 for e in exercises if not e.manual)
    print(
        green(
            bold(
                f"All good: {automatic} tested exercises fail on the stubs and pass on the solutions, "
                f"and {len(exercises) - automatic} README exercises have answers."
            )
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="uv run course.py",
        description="Exercises for Python for TypeScript developers. With no options, "
        "shows the next exercise and runs its tests.",
    )
    parser.add_argument(
        "exercise", nargs="?", help="check one exercise by its id, for example 03-2"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--list", action="store_true", help="list every exercise and its status"
    )
    group.add_argument(
        "--progress", action="store_true", help="show your progress per section"
    )
    group.add_argument(
        "--reset", action="store_true", help="forget your progress (your code is kept)"
    )
    group.add_argument(
        "--done", action="store_true", help="mark the current README exercise as done"
    )
    group.add_argument("--verify", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument(
        "--yes",
        "-y",
        action="store_true",
        help="don't ask for confirmation (with --reset)",
    )
    args = parser.parse_args(argv)

    exercises = discover()
    if args.verify:
        return cmd_verify(exercises)
    if args.reset:
        return cmd_reset(args.yes)
    completed = load_progress()
    if args.list:
        return cmd_list(exercises, completed)
    if args.progress:
        return cmd_progress(exercises, completed)
    if args.done:
        return cmd_done(exercises, completed)
    if args.exercise:
        return cmd_one(args.exercise, exercises, completed)
    return cmd_next(exercises, completed)


if __name__ == "__main__":
    raise SystemExit(main())
