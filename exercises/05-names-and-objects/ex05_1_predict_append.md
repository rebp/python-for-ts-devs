# Exercise 05-1: Predict: a function that appends

Predict the output, then run it (save it as a file, or paste it into `uv run python`):

```python
def add_item(cart, item):
    cart.append(item)

cart = []
add_item(cart, "apple")
print(cart)
```

Write your prediction down first, then check it. Can you explain the result
with "names point to objects"?

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/05-names-and-objects/ex05_1_predict_append.md`.
