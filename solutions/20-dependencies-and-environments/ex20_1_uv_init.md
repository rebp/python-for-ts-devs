# Exercise 20-1: Your first uv project (answer)

```bash
uv init hello-uv
cd hello-uv
uv run main.py   # prints "Hello from hello-uv!"
```

- `pyproject.toml` is the `package.json`: name, version, Python version, dependencies.
- `.python-version` pins the Python version, like `.nvmrc`.
- `main.py` is the starter script, and `README.md` is empty.
- The first `uv run` creates `.venv/`, the project's own environment (think
  `node_modules`, but it also holds the Python interpreter link), and `uv.lock`,
  the lockfile (`package-lock.json`).
