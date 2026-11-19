# Exercise 20-2: Add a dependency

In your `hello-uv` project from the previous exercise:

1. Add the httpx package:

   ```bash
   uv add httpx
   ```

2. Open `pyproject.toml` and find where it was recorded.
3. Write a script that prints the status code of a request to
   `https://example.com`, and run it with `uv run`.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/20-dependencies-and-environments/ex20_2_uv_add.md`.
