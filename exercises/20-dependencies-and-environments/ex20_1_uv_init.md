# Exercise 20-1: Your first uv project

Do this **outside** this exercise pack, for example in your home folder.

1. Install uv if you haven't: see <https://docs.astral.sh/uv/getting-started/installation/>.
2. Create a project and run it:

   ```bash
   uv init hello-uv
   cd hello-uv
   uv run main.py
   ```

3. Look around: which files did `uv init` create? Which one is your
   `package.json`? Where did the virtual environment (`node_modules`) appear
   after `uv run`?

This one is checked by you, not by a test. When you're done, run:

```bash
uv run course.py --done
```

The reference answer is in `solutions/20-dependencies-and-environments/ex20_1_uv_init.md`.
