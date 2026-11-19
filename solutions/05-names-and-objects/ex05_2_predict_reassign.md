# Exercise 05-2: Predict: a function that reassigns (answer)

It prints `['apple']`.

Inside `reset`, `cart = []` points the *local* name `cart` at a brand-new empty
list. The caller's name still points at the original list, which nobody changed.

To empty the caller's list in place, change the object instead of the name:

```python
def reset(cart):
    cart.clear()      # or: del cart[:]
```
