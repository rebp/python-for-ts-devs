# Exercise 4.4-3: Read the small syntax (answer)

`(1)` is an `int`; `(1,)` is a one-element tuple. With
`first, *middle, last = [1, 2, 3, 4]`, the values are `1`, `[2, 3]`, and `4`.
A `NamedTuple` is a good immutable tuple-like point, a dataclass is a good
mutable record, and a `TypedDict` describes the keys of a plain dictionary.
Neither annotations nor a `TypedDict` validate incoming JSON at runtime.
