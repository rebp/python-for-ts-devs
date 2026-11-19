# Exercise 21-1: Catch a type error with mypy

mypy is already a dev dependency of this exercise pack.

1. Create a scratch file, for example `scratch/typo.py` in this folder, with a
   function that has type hints and a call that breaks them on purpose:

   ```python
   def greet(name: str) -> str:
       return "Hi " + name

   greet(42)
   ```

2. Run Python on it first (`uv run scratch/typo.py`). What happens, and when?
3. Run the type checker:

   ```bash
   uv run mypy --strict scratch/typo.py
   ```

4. Read the message, fix the code, and run mypy again until it's clean.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/21-linting-formatting-and-type-checking/ex21_1_mypy.md`.
