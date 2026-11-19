"""Reference solution for exercise 36-2 (A real FastAPI service)."""

from typing import Annotated

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str


class Note(NoteIn):
    id: int


class NotesStore:
    """An in-memory store. In a real service this would talk to a database."""

    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}

    def add(self, text: str) -> Note:
        note = Note(id=len(self._notes) + 1, text=text)
        self._notes[note.id] = note
        return note

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def all(self) -> list[Note]:
        return list(self._notes.values())


_store = NotesStore()


def get_store() -> NotesStore:
    """The dependency that hands each request the store. Tests override it."""
    return _store


# A reusable parameter type: `store: Store` means "inject get_store()".
Store = Annotated[NotesStore, Depends(get_store)]

router = APIRouter(prefix="/notes")


@router.get("")
def list_notes(store: Store) -> list[Note]:
    """Build a notes router: GET /notes, GET /notes/{note_id} and POST /notes.

    - GET /notes returns every note.
    - GET /notes/{note_id} returns one note, or 404 for an unknown id.
    - POST /notes with {"text": "..."} adds a note and returns it with status 201.

    Register the three functions on `router` (not on `app`). The router already
    has the /notes prefix, so the paths are "", "/{note_id}" and "".

    Every function reaches the store through a `store: Store` parameter, never
    through _store directly. That's what lets the tests swap in their own store
    with app.dependency_overrides, like overriding a NestJS provider.
    """
    return store.all()


@router.get("/{note_id}")
def get_note(note_id: int, store: Store) -> Note:
    """GET /notes/{note_id}: the note, or 404."""
    note = store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="note not found")
    return note


@router.post("", status_code=201)
def create_note(data: NoteIn, store: Store) -> Note:
    """POST /notes: add a note and return it with status 201."""
    return store.add(data.text)


app = FastAPI()
app.include_router(router)  # keep this last: it copies the routes registered above
