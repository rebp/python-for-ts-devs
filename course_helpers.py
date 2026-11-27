"""Small helpers the exercise tests share. You don't need to read this file."""

import ast
import inspect
import os
import shutil
import subprocess
import sys
import textwrap
from collections.abc import Callable
from pathlib import Path


def source_tree(obj: Callable[..., object]) -> ast.AST:
    """Parse the source code of a function or class."""
    return ast.parse(textwrap.dedent(inspect.getsource(obj)))


def uses_node(obj: Callable[..., object], node_type: type[ast.AST]) -> bool:
    """True when the source of `obj` contains an AST node of `node_type` (a while loop, a list comprehension...)."""
    return any(isinstance(node, node_type) for node in ast.walk(source_tree(obj)))


def calls_name(obj: Callable[..., object], name: str) -> bool:
    """True when the source of `obj` calls something named `name`, like any(...) or itertools.islice(...)."""
    for node in ast.walk(source_tree(obj)):
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name) and func.id == name:
                return True
            if isinstance(func, ast.Attribute) and func.attr == name:
                return True
    return False


def run_learner_tests(
    test_file: Path,
    tmp_path: Path,
    import_dir: Path,
    replacements: dict[str, str] | None = None,
) -> tuple[bool, str]:
    """Run a test file written by the learner in a separate pytest process.

    `import_dir` is the folder the learner's tests import their code from.
    `replacements` maps module names to source code that should be imported
    instead, which is how the checks swap in deliberately broken versions.
    Returns (all tests passed, pytest output).
    """
    run_dir = tmp_path / f"run{len(list(tmp_path.iterdir()))}"
    run_dir.mkdir()
    (run_dir / "pytest.ini").write_text("[pytest]\n", encoding="utf-8")
    search_path = [str(import_dir)]
    if replacements:
        override = run_dir / "override"
        override.mkdir()
        for module, code in replacements.items():
            (override / f"{module}.py").write_text(
                textwrap.dedent(code), encoding="utf-8"
            )
        search_path.insert(0, str(override))
    env = {
        **os.environ,
        "PYTHONPATH": os.pathsep.join(search_path),
        "PYTHONUTF8": "1",  # same output encoding on every OS
    }
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            str(test_file),
            "-c",
            str(run_dir / "pytest.ini"),
            "--rootdir",
            str(run_dir),
            "--import-mode=append",
            "--noconftest",
            "-p",
            "no:cacheprovider",
            "-q",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
        cwd=run_dir,
        timeout=120,
        check=False,
    )
    return result.returncode == 0, result.stdout + result.stderr


def type_check_strict(
    module_file: Path, usage: str, tmp_path: Path
) -> tuple[bool, str]:
    """Copy an exercise next to a usage file and type-check both with mypy --strict.

    `usage` is Python source that imports the exercise and checks it with
    assert_type and `# type: ignore[...]` lines (an unneeded ignore is an error
    under --strict, so those lines prove that mypy rejects a bad call).
    Returns (mypy passed, mypy output).
    """
    shutil.copy(module_file, tmp_path)
    (tmp_path / "check_usage.py").write_text(textwrap.dedent(usage), encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mypy",
            "--strict",
            "--no-error-summary",
            "--cache-dir",
            str(tmp_path / ".mypy_cache"),
            module_file.name,
            "check_usage.py",
        ],
        cwd=tmp_path,
        env={**os.environ, "PYTHONUTF8": "1"},
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=180,
        check=False,
    )
    return result.returncode == 0, result.stdout + result.stderr
