# Exercise 13.3-3: Check your interpreter

Explain the difference between the normal CPython build and a free-threaded
build. Find a way to check whether the GIL is enabled, and name one reason
you still need locks when sharing mutable state.

Hint: `sys._is_gil_enabled()` reports the running process, not merely the
build configuration.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/recent-python/ex_modern_3_versions.md`.
