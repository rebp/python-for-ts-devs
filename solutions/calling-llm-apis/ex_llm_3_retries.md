# Exercise 12.3-3: Plan retries and timeouts (answer)

A timeout does not prove that the provider did no work, so a retry can repeat
side effects or incur another charge. Use bounded retries only for appropriate
transient failures, and design any side effects to be idempotent. Log request
IDs, timing and error categories rather than private prompts or credentials.
Test timeouts, retries and refusals using a mock transport, never a real API.
