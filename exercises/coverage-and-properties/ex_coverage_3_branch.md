# Exercise 6.3-3: Read a branch report

Run only the two example cases in `test_examples_that_miss_the_bug` with
`pytest-cov` and branch coverage. Explain why a line can execute while one of
its possible branches remains untested. Add an example that takes a missing
branch.

Hint: `-k examples_that_miss_the_bug --cov-branch --cov-report=term-missing`
selects the examples and reports missing paths as well as missing lines.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/coverage-and-properties/ex_coverage_3_branch.md`.
