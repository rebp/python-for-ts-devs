# Exercise 40-3: Read real Python

The fastest way to learn idiomatic Python is to read code by people who write
it every day, and you already have plenty on your machine.

1. Open the installed libraries in this project:
   `.venv/lib/python3.12/site-packages/` on macOS and Linux, or
   `.venv\Lib\site-packages\` on Windows. Every library the course used is
   there as plain Python source.
2. Pick one: `typer/main.py`, `fastapi/routing.py`,
   `sqlalchemy/orm/session.py` or `pydantic_settings/main.py`.
3. Find at least three things from the course in it: a dataclass, a context
   manager, a decorator, a generator, `Annotated`, a Protocol, `__init__.py`
   re-exports, a `match` statement...
4. Find one thing the course didn't cover and look it up.

Also bookmark the official tutorial (`docs.python.org/3/tutorial/`) and the
FastAPI tutorial (`fastapi.tiangolo.com/tutorial/`). Both are well written and
worth reading end to end now that you know the basics.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/40-where-to-go-next/ex40_3_read_real_code.md`.
