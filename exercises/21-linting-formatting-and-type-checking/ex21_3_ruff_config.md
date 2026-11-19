# Exercise 21-3: Configure ruff

In your `hello-uv` project from lesson 20 (not in this exercise pack, whose
settings the course relies on), configure ruff in `pyproject.toml` to:

1. allow lines up to 100 characters, and
2. also check import sorting.

Check it works: write a file with imports in the wrong order
(`import sys` before `import os`) and run `uv run ruff check .`, then
`uv run ruff check --fix .`.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/21-linting-formatting-and-type-checking/ex21_3_ruff_config.md`.
