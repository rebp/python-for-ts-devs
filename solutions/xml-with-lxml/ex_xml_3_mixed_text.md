# Exercise 9.2-3: Follow mixed text (answer)

For `<title>Use <italic>safe</italic> parsing.</title>`:

- The title's `text` is `"Use "`.
- The italic element's `text` is `"safe"`.
- Its `tail` is `" parsing."`.
- `"".join(title.itertext())` is `"Use safe parsing."`.
