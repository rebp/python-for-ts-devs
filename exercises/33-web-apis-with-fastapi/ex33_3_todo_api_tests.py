"""Lesson 33 · Web APIs with FastAPI · exercise 3.

Test the todo API with FastAPI's TestClient and pytest.

Import the app from your exercise 2 (finish that one first):

    from fastapi.testclient import TestClient
    from ex33_2_todo_api import app

Your tests should check that creating a todo returns 201, that a created todo
shows up in GET /todos, and that deleting an unknown id returns 404.

How it's checked: your tests must pass against your todo API, and fail
against broken versions of it. Run them yourself with:

    uv run pytest exercises/33-web-apis-with-fastapi/ex33_3_todo_api_tests.py

Check your work with: uv run course.py
"""

import pytest


def test_placeholder():
    pytest.fail("Replace this placeholder with your own tests")
