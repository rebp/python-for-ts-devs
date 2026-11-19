# Exercise 20-3: A development dependency (answer)

```bash
uv add --dev pytest
uv run pytest     # "no tests ran", which is expected for now
```

pytest is recorded under `[dependency-groups]` → `dev`, not in `[project]`
`dependencies`. Like `devDependencies`, it's installed for development but
isn't a dependency of your package when someone else installs it.

pytest exits with code 5 when it collects no tests, which is why the command
looks like it "failed".
