# Exercise 07-3: When `or` defaults become a bug (answer)

1. `or` returns the first truthy operand (or the last operand if none is truthy).
   `0` is falsy, so `or` moves on and returns `8080`. It's JavaScript's `||`.
2. It's a bug whenever a falsy value is valid input: a count or port of `0`,
   an empty string the user typed on purpose, an empty list meaning "no filters",
   `False` meaning "turned off".
3. Compare with `None` explicitly, which is Python's version of `??`:

   ```python
   port = value if value is not None else 8080
   ```
