# Exercise 40-2: Port something real

Pick something small that your team already has in TypeScript: a script in
`scripts/`, a build helper, a single API endpoint, a data migration. Rewrite it
in Python.

While you do it, note down:

1. Which npm packages you replaced, and with what (lesson 40's phrasebook
   helps).
2. Every place you started to write TypeScript in Python: an index loop, a
   getter, `== None`, a mutable default, a class that could be a function.
3. What got shorter, and what got longer.

Then run `uv run ruff check` and `uv run mypy` on it, and fix what they find.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/40-where-to-go-next/ex40_2_port_a_tool.md`.
