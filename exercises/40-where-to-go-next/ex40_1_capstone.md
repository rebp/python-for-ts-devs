# Exercise 40-1: Build one small service end to end

Put the course together in a scratch project: a notes service you could
actually deploy.

1. `uv init notes-service` and add FastAPI, SQLAlchemy and pydantic-settings.
2. Store notes in SQLite through SQLAlchemy (lesson 34), with the database URL
   coming from a `Settings` class (37-1).
3. Put the routes in an `APIRouter` and inject the database session with a
   `Depends` function that uses `yield` (lessons 28 and 36).
4. Protect writes with an API key (36-1), and add `/health` and the access log
   (37-2).
5. Write pytest tests with `TestClient` that override the session dependency
   with an in-memory database (`sqlite://`).
6. Get `uv run ruff check`, `uv run ruff format --check` and `uv run mypy .`
   to pass (lesson 21).
7. Ship it in Docker (37-3).

Expect it to take an afternoon. Look things up in the earlier lessons as you
go: that's the point.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/40-where-to-go-next/ex40_1_capstone.md`.
