# Exercise 6.3-3: Read a branch report (answer)

For example:

```bash
uv run pytest exercises/coverage-and-properties/test_ex_coverage_1_clamp.py -k examples_that_miss_the_bug --cov=ex_coverage_1_clamp --cov-branch --cov-report=term-missing
```

Executing an `if` line does not prove that both its true and false paths ran.
The report points to the missing branch; add a case such as
`clamp(11, 0, 10) == 10` and rerun the tests without `-k`.
