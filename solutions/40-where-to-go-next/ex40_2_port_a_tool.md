# Exercise 40-2: Port something real (answer)

There's no single answer, since it depends on what you ported. These are the
things people porting from TypeScript most often notice.

**Usually shorter in Python**

- Data shaping: comprehensions, `sorted(key=...)`, `collections.Counter` and
  `itertools` replace chains of `map`, `filter`, `reduce` and lodash.
- File and path work: `pathlib` covers `fs`, `path` and `glob` in one API.
- Scripts in general: no build step, no `tsconfig.json`, and `uv run script.py`
  runs it with its dependencies.

**Usually longer, or less comfortable**

- Anything that leans on TypeScript's type system: union narrowing, mapped
  and conditional types. Python's typing is good but simpler, and only checked
  when you run mypy.
- Async code: you start the event loop yourself (`asyncio.run`), and blocking
  libraries don't mix with it.

**TypeScript habits to look for in your code**

| Habit | Pythonic version |
| --- | --- |
| `for i in range(len(items))` | `for item in items`, or `enumerate(items)` |
| `if x == None` | `if x is None` |
| `def f(items=[])` | `def f(items=None)` (lesson 8) |
| getters and setters | plain attributes, or `@property` when needed |
| a class with one method | a function |
| `try` blocks around everything | let exceptions propagate, catch where you can act |
| `camelCase` names | `snake_case` (ruff's `N` rules can check this) |
