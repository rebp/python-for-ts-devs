# Exercise 40-1: Build one small service end to end (answer)

One reasonable layout, with the key pieces. Yours doesn't need to match it.

```text
notes-service/
  pyproject.toml
  uv.lock
  Dockerfile
  .dockerignore
  notes/
    __init__.py
    settings.py     Settings(BaseSettings) and get_settings()
    db.py           engine, Base, get_session()
    models.py       the SQLAlchemy Note table
    schemas.py      Pydantic NoteIn / NoteOut
    routes.py       APIRouter(prefix="/notes")
    main.py         app = FastAPI(), include_router, middleware, /health
  tests/
    test_notes.py
```

## settings.py

```python
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NOTES_")
    database_url: str = "sqlite:///notes.db"
    api_key: str


@lru_cache  # read the environment once, not on every request
def get_settings() -> Settings:
    return Settings()
```

## db.py: a session per request

```python
from collections.abc import Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from notes.settings import get_settings

engine = create_engine(get_settings().database_url)


class Base(DeclarativeBase):
    pass


def get_session() -> Iterator[Session]:
    with Session(engine) as session:  # closed after the response is sent
        yield session
```

## routes.py

```python
from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from notes.db import get_session
from notes.models import Note
from notes.schemas import NoteIn, NoteOut
from notes.settings import Settings, get_settings

DbSession = Annotated[Session, Depends(get_session)]


def require_api_key(
    settings: Annotated[Settings, Depends(get_settings)],
    x_api_key: Annotated[str | None, Header()] = None,
) -> None:
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=401, detail="invalid or missing API key")


router = APIRouter(prefix="/notes")


@router.get("")
def list_notes(session: DbSession) -> list[NoteOut]:
    notes = session.scalars(select(Note).order_by(Note.id))
    return [NoteOut.model_validate(note, from_attributes=True) for note in notes]


@router.post("", status_code=201, dependencies=[Depends(require_api_key)])
def create_note(data: NoteIn, session: DbSession) -> NoteOut:
    note = Note(text=data.text)
    session.add(note)
    session.commit()
    return NoteOut.model_validate(note, from_attributes=True)
```

## tests/test_notes.py: swap the database

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from notes.db import Base, get_session
from notes.main import app
from notes.settings import Settings, get_settings


@pytest.fixture
def client():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    Base.metadata.create_all(engine)

    def session_override():
        with Session(engine) as session:
            yield session

    app.dependency_overrides[get_session] = session_override
    app.dependency_overrides[get_settings] = lambda: Settings(api_key="test")
    yield TestClient(app)
    app.dependency_overrides.clear()


def test_create_needs_the_key(client):
    assert client.post("/notes", json={"text": "hi"}).status_code == 401
    response = client.post("/notes", json={"text": "hi"}, headers={"X-API-Key": "test"})
    assert response.status_code == 201
    assert client.get("/notes").json() == [{"id": 1, "text": "hi"}]
```

`StaticPool` keeps one connection open, so every session in the test sees
the same in-memory database. Without it, each connection would get its own
empty database.

If you got this far, you can build and ship a Python web service. What's left
is practice and the libraries your team happens to use.
