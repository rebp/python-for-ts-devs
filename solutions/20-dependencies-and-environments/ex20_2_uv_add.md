# Exercise 20-2: Add a dependency (answer)

`uv add httpx` adds it to the `dependencies` list under `[project]` in
`pyproject.toml` (like `dependencies` in `package.json`), installs it into
`.venv`, and updates `uv.lock`.

```python
# status.py
import httpx

response = httpx.get("https://example.com")
print(response.status_code)  # 200
```

```bash
uv run status.py
```
