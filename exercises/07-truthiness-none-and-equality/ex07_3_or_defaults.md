# Exercise 07-3: When `or` defaults become a bug

In the REPL, evaluate `0 or 8080`.

Then write two or three sentences, in a comment or a notes file, that answer:

1. Why does `0 or 8080` return `8080`?
2. When does `value or default` become a bug? Think of at least two kinds of
   values where it goes wrong.
3. What should you write instead?

TypeScript hint: it's the same story as `||` versus `??`.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/07-truthiness-none-and-equality/ex07_3_or_defaults.md`.
