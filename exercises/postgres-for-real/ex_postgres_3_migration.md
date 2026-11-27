# Exercise 10.3-3: Review a migration

An Alembic autogenerate result drops `old_name` and adds `new_name`. What might
have happened, what would you review before applying it, and why should a
request transaction commit before the response is sent?

Hint: autogenerate proposes migrations; it does not understand every intent.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/postgres-for-real/ex_postgres_3_migration.md`.
