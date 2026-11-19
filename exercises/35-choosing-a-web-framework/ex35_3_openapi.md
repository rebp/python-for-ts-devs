# Exercise 35-3: Read your API's OpenAPI schema

FastAPI writes an OpenAPI schema for every app. It's what powers `/docs`, and
lesson 37 uses it to generate a TypeScript client.

1. Start the search API from exercise 35-2 in a scratch project, or the todo
   API from 33-2:

   ```bash
   uv run fastapi dev ex35_2_search.py
   ```

2. Open `http://127.0.0.1:8000/docs` and try the search endpoint with and
   without `q`.
3. Open `http://127.0.0.1:8000/openapi.json` and find:
   - the `Item` schema under `components.schemas`,
   - the `limit` parameter, with its `minimum` and `maximum`,
   - the 422 response that FastAPI documented for you.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/35-choosing-a-web-framework/ex35_3_openapi.md`.
