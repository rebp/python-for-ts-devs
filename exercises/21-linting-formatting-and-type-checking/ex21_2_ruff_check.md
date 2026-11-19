# Exercise 21-2: Lint and auto-fix with ruff

1. Create a scratch file, for example `scratch/messy.py`, with an unused import
   and an unused variable:

   ```python
   import os


   def f() -> None:
       x = 1
   ```

2. Run the linter and read what it reports:

   ```bash
   uv run ruff check scratch/messy.py
   ```

3. Now let it fix what it can, and compare:

   ```bash
   uv run ruff check --fix scratch/messy.py
   ```

4. Bonus: run `uv run ruff format scratch/messy.py`. That's Prettier.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/21-linting-formatting-and-type-checking/ex21_2_ruff_check.md`.
