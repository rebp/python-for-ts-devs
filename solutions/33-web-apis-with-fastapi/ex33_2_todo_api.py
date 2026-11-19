"""Reference solution for exercise 33-2 (Web APIs with FastAPI)."""

from itertools import count

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TodoIn(BaseModel):
    title: str


class Todo(TodoIn):
    id: int


todos: dict[int, Todo] = {}
_ids = count(1)  # a counter, so ids are never reused after a delete


@app.post("/todos", status_code=201)
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
    todo = Todo(id=next(_ids), title=data.title)
    todos[todo.id] = todo
    return todo


@app.get("/todos")
def list_todos() -> list[Todo]:
    """GET /todos"""
    return list(todos.values())


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    """DELETE /todos/{todo_id}: 204, or 404 for an unknown id."""
    if todos.pop(todo_id, None) is None:
        raise HTTPException(status_code=404, detail="todo not found")
