# Exercise 13.2-3: Set a dependency rule (answer)

```toml
[tool.importlinter]
root_package = "shop"

[[tool.importlinter.contracts]]
name = "Dependencies point toward the domain"
type = "layers"
layers = ["shop.api", "shop.application", "shop.domain"]
```

The list goes from highest to lowest: the domain cannot import the application
or API. For a uv workspace, declare the domain distribution as a dependency
and add `shop-domain = { workspace = true }` under `[tool.uv.sources]`.
