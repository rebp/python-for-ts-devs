# Exercise 11.2-3: Plan local and CI checks

Draft a GitHub Actions matrix for the Python versions your project supports,
using `astral-sh/setup-uv` with caching and `uv sync --locked`. Add local
pre-commit hooks for Ruff and mypy, and explain why CI still runs the checks.

Hint: quote version strings and let mypy check the whole package rather than
only one changed file.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/ci-and-precommit/ex_ci_3_config.md`.
