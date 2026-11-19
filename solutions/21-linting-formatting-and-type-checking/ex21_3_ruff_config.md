# Exercise 21-3: Configure ruff (answer)

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
extend-select = ["I"]   # "I" = the isort rules for import order
```

`extend-select` adds rules to ruff's defaults; `select` would replace them.
With the `I` rules on, `ruff check` reports `I001 Import block is un-sorted or
un-formatted`, and `--fix` sorts the imports for you.
