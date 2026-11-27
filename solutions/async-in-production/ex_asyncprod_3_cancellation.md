# Exercise 8.2-3: Reason about cancellation (answer)

The timeout cancels the waiting task and raises `TimeoutError` outside its
context. A blocking call already running in a thread continues; cancelling its
await does not stop that thread. To stop early, arrange for the blocking
function to check a `threading.Event` or another cooperative stop signal.
Clean up in `finally`, and do not swallow `CancelledError` in async code.
