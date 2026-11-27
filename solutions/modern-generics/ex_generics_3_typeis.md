# Exercise 3.8-3: Narrow both branches (answer)

```python
from typing import TypeIs, assert_type


def is_text(value: str | int) -> TypeIs[str]:
    return isinstance(value, str)


def show(value: str | int) -> None:
    if is_text(value):
        assert_type(value, str)
    else:
        assert_type(value, int)
```

The checker narrows the true branch to `str` and the false branch to `int`.
The call to `isinstance`, not the annotation, performs the runtime check.
