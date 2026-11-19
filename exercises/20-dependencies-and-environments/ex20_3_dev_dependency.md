# Exercise 20-3: A development dependency

Still in `hello-uv`:

1. Add pytest as a **development** dependency (TypeScript: `npm install -D`).
2. Run it.
3. With no tests yet, read what it reports. Where in `pyproject.toml` did
   pytest end up, and how is that different from httpx?

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/20-dependencies-and-environments/ex20_3_dev_dependency.md`.
