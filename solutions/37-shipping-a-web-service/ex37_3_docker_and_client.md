# Exercise 37-3: Ship it in Docker and give the front end a typed client (answer)

## Dockerfile

```dockerfile
FROM python:3.15-slim

# Copy the uv binary from its official image instead of installing it with pip.
COPY --from=ghcr.io/astral-sh/uv:0.13.5 /uv /uvx /bin/

WORKDIR /app

# Dependencies first, so Docker caches this layer until uv.lock changes
# (the same trick as copying package*.json before npm ci).
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY . .

EXPOSE 8000
# 0.0.0.0, not 127.0.0.1: otherwise nothing outside the container can connect.
CMD ["uv", "run", "--no-sync", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

`uv sync --frozen` is `npm ci`: it installs exactly what's in the lockfile and
fails if the lockfile is out of date. `--no-dev` leaves out pytest, ruff and
mypy.

## .dockerignore

```text
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.mypy_cache/
```

Without it, `COPY . .` copies your local `.venv`, which was built for your
machine (macOS, for example) and won't work inside a Linux container.

## The typed client

`openapi-typescript` turns `/openapi.json` into a `paths` type, and
`openapi-fetch` is a tiny `fetch` wrapper that uses it:

```typescript
import createClient from "openapi-fetch";
import type { paths } from "./api";

const api = createClient<paths>({ baseUrl: "http://localhost:8000" });

const { data, error } = await api.GET("/notes/{note_id}", {
  params: { path: { note_id: 1 } },
});
if (data) console.log(data.text); // data is typed as { id: number; text: string }

await api.POST("/notes", { body: { text: "From TypeScript" } });
// api.POST("/notes", { body: { txt: "typo" } })  ← compile error
```

When a Pydantic model changes, regenerate `api.d.ts` and the TypeScript
compiler points at every call that needs updating. Many teams run the
`openapi-typescript` command in CI, so the front end and the back end can't
drift apart.

## Running more than one process

uvicorn runs a single process. In production, either run several containers
behind a load balancer (the usual choice with Kubernetes or ECS), or start
several workers in one container:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

It's the same idea as Node's `cluster` module or `pm2 -i 4`.
