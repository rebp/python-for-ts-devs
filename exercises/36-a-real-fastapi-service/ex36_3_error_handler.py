"""Lesson 36 · A real FastAPI service · exercise 3.

Check your work with: uv run course.py
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class NoteNotFound(Exception):
    def __init__(self, note_id: int) -> None:
        super().__init__(f"note {note_id} not found")
        self.note_id = note_id


NOTES = {1: "Buy milk", 2: "Learn FastAPI"}


def find_note(note_id: int) -> str:
    """The service layer: it knows nothing about HTTP and raises a domain error."""
    if note_id not in NOTES:
        raise NoteNotFound(note_id)
    return NOTES[note_id]


app = FastAPI()


async def note_not_found_handler(request: Request, exc: NoteNotFound) -> JSONResponse:
    """Turn NoteNotFound into an HTTP response in one place, for every route.

    Any route that lets a NoteNotFound escape must answer with status 404 and
    this JSON body:

        {"error": "note_not_found", "note_id": 7}

    Register the function with @app.exception_handler(NoteNotFound) and return
    a fastapi.responses.JSONResponse. It's the FastAPI version of a NestJS
    exception filter or an Express error-handling middleware. Leave the routes
    alone: they should keep calling find_note without any try/except.
    """
    raise NotImplementedError("Your code here")


@app.get("/notes/{note_id}")
def read_note(note_id: int) -> dict[str, str]:
    return {"text": find_note(note_id)}


@app.get("/notes/{note_id}/shout")
def shout_note(note_id: int) -> dict[str, str]:
    return {"text": find_note(note_id).upper()}
