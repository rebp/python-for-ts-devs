"""Reference solution for exercise 14-3 (Typing in depth)."""

from typing import Self


class Stack[T]:
    """Make Stack a generic class, the Python version of class Stack<T>.

    - Stack[int]() holds ints, Stack[str]() holds strings.
    - push(item) adds an item and returns the stack itself, so calls chain:
      Stack[int]().push(1).push(2). Annotate the return type as Self.
    - pop() removes and returns the last item, or raises IndexError when the
      stack is empty.
    - peek() returns the last item without removing it, or None when empty.
    - len(stack) is the number of items (define __len__).

    The tests run mypy --strict, and check that Stack[int]().push("three") is
    a type error and that pop() on a Stack[int] is an int.
    """

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> Self:
        self._items.append(item)
        return self

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from an empty stack")
        return self._items.pop()

    def peek(self) -> T | None:
        return self._items[-1] if self._items else None

    def __len__(self) -> int:
        return len(self._items)
