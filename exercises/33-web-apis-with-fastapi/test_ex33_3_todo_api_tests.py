"""Tests for exercise 33-3 (Web APIs with FastAPI).

Edit: ex33_3_todo_api_tests.py::
"""

import pytest

from course_helpers import run_learner_tests

LEARNER_FILE = "ex33_3_todo_api_tests.py"

BROKEN_APP = """
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()


class TodoIn(BaseModel):
    title: str


todos = {}


@app.post("/todos", status_code=CREATE_STATUS)
def create_todo(data: TodoIn):
    todo = {"id": len(todos) + 1, "title": data.title}
    todos[todo["id"]] = todo
    return todo


@app.get("/todos")
def list_todos():
    return LIST_RESULT


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    if todos.pop(todo_id, None) is None and UNKNOWN_IS_404:
        raise HTTPException(status_code=404, detail="todo not found")
    return Response(status_code=204)
"""


def broken(
    create_status="201", list_result="list(todos.values())", unknown_is_404="True"
):
    return (
        BROKEN_APP.replace("CREATE_STATUS", create_status)
        .replace("LIST_RESULT", list_result)
        .replace("UNKNOWN_IS_404", unknown_is_404)
    )


BROKEN = {
    "creating a todo returns 200 instead of 201": broken(create_status="200"),
    "GET /todos forgets the created todos": broken(list_result="[]"),
    "deleting an unknown id returns 204 instead of 404": broken(unknown_is_404="False"),
}


@pytest.fixture(scope="module")
def working_run(lesson_dir, tmp_path_factory):
    return run_learner_tests(
        lesson_dir / LEARNER_FILE, tmp_path_factory.mktemp("ok"), lesson_dir
    )


def test_your_tests_pass_against_your_todo_api(working_run):
    passed, output = working_run
    assert passed, (
        "your tests fail against your todo API from exercise 33-2 "
        "(is that one finished?):\n" + output
    )


@pytest.mark.parametrize("bug", list(BROKEN))
def test_your_tests_catch_a_broken_api(bug, lesson_dir, tmp_path, working_run):
    assert working_run[0], "first make your tests pass against your todo API"
    passed, _ = run_learner_tests(
        lesson_dir / LEARNER_FILE,
        tmp_path,
        lesson_dir,
        {"ex33_2_todo_api": BROKEN[bug]},
    )
    assert not passed, f"your tests still pass when {bug}."
