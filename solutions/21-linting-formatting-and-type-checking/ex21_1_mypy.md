# Exercise 21-1: Catch a type error with mypy (answer)

Running the file raises `TypeError: can only concatenate str (not "int") to str`,
but only when that line executes. Type hints are ignored at runtime.

mypy finds it without running anything:

```text
scratch/typo.py:4: error: Argument 1 to "greet" has incompatible type "int"; expected "str"  [arg-type]
```

Fix the call:

```python
greet("42")
```

mypy is to Python what `tsc --noEmit` is to TypeScript. `--strict` is like
`"strict": true`: it also complains about functions without type hints.
