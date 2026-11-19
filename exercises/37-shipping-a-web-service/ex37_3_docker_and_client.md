# Exercise 37-3: Ship it in Docker and give the front end a typed client

You need Docker and Node.js for this one. Work in a scratch project, outside
this folder.

1. Create a project with the notes router from exercise 36-2 as `app.py`:

   ```bash
   uv init notes-service && cd notes-service
   uv add "fastapi[standard]"
   ```

2. Write a `Dockerfile` that installs the dependencies with uv from
   `uv.lock`, and starts the app with uvicorn on port 8000. Add a
   `.dockerignore` so your local `.venv` isn't copied into the image.
3. Build and run it, then open `http://localhost:8000/docs`:

   ```bash
   docker build -t notes-service .
   docker run --rm -p 8000:8000 notes-service
   ```

4. With the container running, generate TypeScript types from the OpenAPI
   schema in a front-end project, and call `GET /notes/{note_id}` with
   full type checking:

   ```bash
   npx openapi-typescript http://localhost:8000/openapi.json -o src/api.d.ts
   npm install openapi-fetch
   ```

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/37-shipping-a-web-service/ex37_3_docker_and_client.md`.
