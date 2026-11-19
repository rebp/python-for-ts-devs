"""Reference solution for exercise 36-1 (A real FastAPI service)."""

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException

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
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="invalid or missing API key")


app = FastAPI()


@app.get("/public")
def public() -> dict[str, str]:
    return {"message": "anyone can see this"}


@app.get("/private", dependencies=[Depends(require_api_key)])
def private() -> dict[str, str]:
    return {"message": "you have the key"}
