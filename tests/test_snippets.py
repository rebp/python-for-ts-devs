"""Every Python example on the course site either runs or says how to run it."""

import html
import re
import subprocess
import sys
from pathlib import Path

import pytest

PAGE = Path(__file__).resolve().parent.parent / "index.html"
PAGE_TEXT = PAGE.read_text("utf-8")
EXAMPLE = re.compile(
    r'<pre><code class="language-python"([^>]*)>(.*?)</code></pre>', re.DOTALL
)
ATTRIBUTE = re.compile(r'\s(data-[a-z]+)(?:="([^"]*)")?')
RUN_MODES = {"", "async", "files"}
STATIC_REASONS = {
    "network",
    "server",
    "threads",
    "tests",
    "debugger",
    "course-code",
    "unsupported-library",
    "terminal",
    "excerpt",
}

EXAMPLES = [
    (dict(ATTRIBUTE.findall(attributes)), html.unescape(body))
    for attributes, body in EXAMPLE.findall(PAGE_TEXT)
]
RUNNING = [source for attrs, source in EXAMPLES if attrs.get("data-run") in RUN_MODES]
FAILING = [source for attrs, source in EXAMPLES if attrs.get("data-run") == "error"]


def run(source: str, directory: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-I", "-c", source],
        check=False,
        capture_output=True,
        text=True,
        timeout=20,
        cwd=directory,
    )


def test_every_example_runs_or_explains_why() -> None:
    problems = []
    for attrs, source in EXAMPLES:
        first_line = source.splitlines()[0] if source else ""
        if ("data-run" in attrs) == ("data-static" in attrs):
            problems.append(f"needs data-run or data-static: {first_line}")
        elif "data-run" in attrs and attrs["data-run"] not in RUN_MODES | {"error"}:
            problems.append(f"unknown data-run {attrs['data-run']!r}: {first_line}")
        elif "data-static" in attrs and attrs["data-static"] not in STATIC_REASONS:
            problems.append(
                f"unknown data-static {attrs['data-static']!r}: {first_line}"
            )
    assert not problems, "\n".join(problems)


def test_page_explains_every_static_reason() -> None:
    notes = re.search(r"var STATIC_NOTES = \{(.*?)\n  \};", PAGE_TEXT, re.DOTALL)
    assert notes is not None
    keys = set(re.findall(r'^\s*"?([a-z-]+)"?:', notes.group(1), re.MULTILINE))
    assert keys == STATIC_REASONS


@pytest.mark.parametrize(
    "source", RUNNING, ids=[f"run-{i}" for i in range(len(RUNNING))]
)
def test_runnable_example_runs(source: str, tmp_path: Path) -> None:
    result = run(source, tmp_path)
    assert result.returncode == 0, f"{source}\n\n{result.stderr}"
    assert result.stdout.strip(), f"{source}\n\nprinted nothing"


@pytest.mark.parametrize(
    "source", FAILING, ids=[f"error-{i}" for i in range(len(FAILING))]
)
def test_error_example_fails_on_purpose(source: str, tmp_path: Path) -> None:
    result = run(source, tmp_path)
    assert result.returncode != 0, f"{source}\n\nexpected an error"
    assert "Error" in result.stderr, f"{source}\n\n{result.stderr}"
    assert "ModuleNotFoundError" not in result.stderr, result.stderr
