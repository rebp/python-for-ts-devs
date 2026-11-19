# Exercise 21-2: Lint and auto-fix with ruff (answer)

```python
import os        # F401: `os` imported but unused. --fix removes it


def f() -> None:
    x = 1        # F841: local variable `x` is assigned to but never used
```

`ruff check` reports both. `ruff check --fix` removes the unused import, which
is always safe. It leaves F841 for you to fix, because deleting an assignment
could hide a real bug (by default that fix is marked "unsafe";
`--unsafe-fixes` would apply it).

ruff is ESLint and Prettier in one tool: `ruff check` lints, `ruff format`
formats.
