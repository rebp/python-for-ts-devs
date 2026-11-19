# Exercise 35-3: Read your API's OpenAPI schema (answer)

`uv run fastapi dev` needs the FastAPI command-line tool. In a scratch project,
install it with `uv add "fastapi[standard]"`, as in lesson 33.

The relevant parts of `/openapi.json` look like this (shortened):

```json
{
  "paths": {
    "/items/search": {
      "get": {
        "parameters": [
          { "name": "q", "in": "query", "required": true, "schema": { "type": "string" } },
          { "name": "limit", "in": "query", "required": false,
            "schema": { "type": "integer", "maximum": 50, "minimum": 1, "default": 10 } },
          { "name": "max_price", "in": "query", "required": false,
            "schema": { "anyOf": [{ "type": "number" }, { "type": "null" }] } }
        ],
        "responses": {
          "200": { "content": { "application/json": { "schema": {
            "type": "array", "items": { "$ref": "#/components/schemas/Item" } } } } },
          "422": { "description": "Validation Error" }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Item": {
        "type": "object",
        "properties": { "name": { "type": "string" }, "price": { "type": "number" } },
        "required": ["name", "price"]
      }
    }
  }
}
```

Everything here comes from your type hints: `q: str` became a required string,
`Query(ge=1, le=50)` became `minimum` and `maximum`, `float | None` became an
optional number, and `-> list[Item]` became the response schema. Nobody wrote
any of it by hand.
