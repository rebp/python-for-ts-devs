# Exercise 3.7-3: Predict hashability

A class defines `__eq__` but does not define `__hash__`. Predict what happens
when you add an instance to a set, and explain one safe way to make instances
hashable.

Hint: equal objects must have equal, stable hashes.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/python-data-model/ex_datamodel_3_hash.md`.
