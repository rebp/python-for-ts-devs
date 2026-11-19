# Exercise 01-3: Explore the REPL (answer)

```python
>>> 2 ** 10   # 1024: power, like Math.pow(2, 10) or 2 ** 10 in JS
>>> 7 / 2     # 3.5: / always returns a float, even for 8 / 2 (4.0)
>>> 7 // 2    # 3: floor division, like Math.floor(7 / 2)
```

Bonus: `-7 // 2` is `-4`. Floor division rounds down, towards minus infinity,
so it matches `Math.floor(-7 / 2)`, not `Math.trunc(-7 / 2)` (which is -3).
