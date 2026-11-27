# Exercise 3.8-3: Narrow both branches

Write an `is_text(value: str | int) -> TypeIs[str]` predicate using
`isinstance`. In a function receiving `str | int`, call it in an `if`.
What type does a checker infer in each branch? What actually performs the
runtime check?

Hint: import `TypeIs` from `typing`; it describes both branches.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/modern-generics/ex_generics_3_typeis.md`.
