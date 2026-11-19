# Exercise 05-2: Predict: a function that reassigns

Predict the output, then run it:

```python
def reset(cart):
    cart = []

cart = ["apple"]
reset(cart)
print(cart)
```

How would you change `reset` so that it really empties the caller's list?

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/05-names-and-objects/ex05_2_predict_reassign.md`.
