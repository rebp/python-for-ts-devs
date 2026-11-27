# Exercise 13.3-3: Check your interpreter (answer)

The normal CPython build uses the GIL. A free-threaded build can run Python
threads in parallel, although some extensions can re-enable the GIL.
`sys._is_gil_enabled()` checks the running process; the build flag is
`sysconfig.get_config_var("Py_GIL_DISABLED")`. Shared mutable state still
needs synchronization because multi-step operations can race.
