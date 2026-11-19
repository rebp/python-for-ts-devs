# Exercise 08-3: Predict: reading a global you also assign (answer)

It raises `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`.

Python decides a name's scope when it compiles the function, not line by line.
Because `x` is assigned somewhere in `show`, it's local for the *whole*
function, so `print(x)` reads a local that has no value yet. (In TypeScript,
`let x` in the function would give the same "used before initialization" error.)

Two fixes that print `10`:

```python
def show():
    print(x)        # remove the assignment: x is the global again


def show():
    global x        # or declare that you mean the global (then x = 5 changes it)
    print(x)
    x = 5
```

The first one is almost always what you want.
