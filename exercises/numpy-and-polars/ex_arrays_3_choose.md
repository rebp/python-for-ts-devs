# Exercise 12.2-3: Choose a data tool

Choose between NumPy, pandas and Polars for numerical array math, an existing
pandas analysis, and a large file query that benefits from a lazy plan. Explain
when a Polars `LazyFrame` actually performs its work.

Hint: `collect()` executes a lazy query; vectorization is not a guarantee of
speed for every input size.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/numpy-and-polars/ex_arrays_3_choose.md`.
