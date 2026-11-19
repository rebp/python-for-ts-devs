# Exercise 08-3: Predict: reading a global you also assign

Predict what happens, then run it:

```python
x = 10

def show():
    print(x)
    x = 5

show()
```

Write down your prediction and an explanation. Then find two ways to make
`show()` print `10`.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/08-scope-and-the-mutable-default-trap/ex08_3_predict_scope.md`.
