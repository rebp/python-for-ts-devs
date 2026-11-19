"""Lesson 36 · A real FastAPI service · exercise 1.

Check your work with: uv run course.py
"""

from typing import Annotated

from fastapi import FastAPI, Header

API_KEY = "let-me-in"


def require_api_key(x_api_key: Annotated[str | None, Header()] = None) -> None:
    """Write a dependency that only lets requests through when the X-API-Key
    header equals API_KEY, and use it to protect GET /private.

    - No header, or the wrong key: raise HTTPException with status 401.
    - The right key: return None, and the route runs as usual.
    - GET /public must keep working without a key.

    Protect the route with dependencies=[Depends(require_api_key)] in its
    @app.get(...) call, the way a NestJS guard protects a controller.

    Hint: a parameter named x_api_key annotated with Header() reads the
    X-API-Key header. FastAPI turns the underscores into hyphens.
    """
    raise NotImplementedError("Your code here")


app = FastAPI()


@app.get("/public")
def public() -> dict[str, str]:
    return {"message": "anyone can see this"}


@app.get("/private")
def private() -> dict[str, str]:
    return {"message": "you have the key"}
