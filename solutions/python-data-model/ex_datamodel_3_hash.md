# Exercise 3.7-3: Predict hashability (answer)

Python sets `__hash__ = None` when a class defines `__eq__` without defining
`__hash__`, so adding an instance to a set raises `TypeError`. For an immutable
value, implement both methods using the same stable fields, or use a frozen
dataclass with appropriate generated equality and hashing.
