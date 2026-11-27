# Exercise 13.2-3: Set a dependency rule

In a scratch project with `shop.api`, `shop.application`, and `shop.domain`,
write an import-linter layers contract that allows dependencies only toward
the domain. Explain which way the layers are listed and how a uv workspace
could share a local domain package.

Hint: layers are listed from highest to lowest; workspace dependencies need
both a project dependency and a `tool.uv.sources` entry.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/large-codebase/ex_architecture_3_contract.md`.
