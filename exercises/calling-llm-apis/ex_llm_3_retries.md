# Exercise 12.3-3: Plan retries and timeouts

An API call times out after the provider may already have processed it.
Explain why blindly retrying can duplicate work or cost, what you would log
without exposing private content, and how you would test the behavior offline.

Hint: distinguish retryable failures from validation errors and refusals.

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/calling-llm-apis/ex_llm_3_retries.md`.
