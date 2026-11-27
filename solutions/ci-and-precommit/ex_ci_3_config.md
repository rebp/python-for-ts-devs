# Exercise 11.2-3: Plan local and CI checks (answer)

Use the workflow and local hooks shown in the lesson. Quote each matrix
version, enable the setup-uv cache, and install with `uv sync --locked`.
Run Ruff and mypy with the same project environment locally and in CI.
CI still matters because local hooks can be skipped or configured differently.
