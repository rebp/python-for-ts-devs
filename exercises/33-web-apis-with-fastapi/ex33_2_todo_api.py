"""Lesson 33 · Web APIs with FastAPI · exercise 2.

Check your work with: uv run course.py
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TodoIn(BaseModel):
    title: str


class Todo(TodoIn):
    id: int


todos: dict[int, Todo] = {}


def create_todo(data: TodoIn) -> Todo:
    """Build an in-memory todo API: POST /todos, GET /todos and DELETE
    /todos/{todo_id}, returning 404 for unknown IDs.

    - POST /todos with {"title": "..."} creates a todo with a new id and
      returns it with status 201.
    - GET /todos returns all todos as a list.
    - DELETE /todos/{todo_id} removes it and returns 204, or 404 for an
      unknown id (raise fastapi.HTTPException).

    The models and the storage are ready. Write the three functions and register
    each one with the right @app decorator.
    """
    raise NotImplementedError("Your code here")


def list_todos() -> list[Todo]:
    """GET /todos"""
    raise NotImplementedError("Your code here")


def delete_todo(todo_id: int) -> None:
    """DELETE /todos/{todo_id}: 204, or 404 for an unknown id."""
    raise NotImplementedError("Your code here")
