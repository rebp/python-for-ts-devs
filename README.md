# Python for TypeScript developers

A hands-on Python course for people who already write TypeScript. Each lesson
puts TypeScript and Python side by side, explains only what's different, and
ends with three exercises that check themselves.

- **44 lessons, 132 exercises.** 111 are checked by tests; 21 (predict the
  output, REPL experiments, tooling setup, open-ended projects) are short
  READMEs you check yourself.
- **One command** shows the next exercise, runs its tests and remembers your
  progress.
- **Reference solutions** for everything, in `solutions/`.

Everything works the same on Windows, macOS and Linux, and every command in
this README and in the course is the same on all three. On Windows, use
PowerShell or the VS Code terminal.

## What you need

- **Git**, to get the course.
- **[uv](https://docs.astral.sh/uv/)**, the Python project tool (think `npm`
  and `nvm` in one). You don't need to install Python yourself: uv downloads
  Python 3.15 the first time you run the course.
- **A browser** for the lessons, and **an editor** for the exercises. VS Code
  works well (see [Tips](#tips)).
- Only for exercise 11.1-3: Docker and Node.js.

Install uv with one command:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then open a new terminal so the `uv` command is found. Homebrew
(`brew install uv`) and winget (`winget install astral-sh.uv`) work too.

## Getting started

1. Get the course and go into its folder:

   ```bash
   git clone https://github.com/rebp/python-for-ts-devs.git
   cd python-for-ts-devs
   ```

2. Install everything the exercises need. This creates the project's `.venv`
   folder (its `node_modules`) with Python, pytest, ruff, mypy and the
   libraries the later lessons use:

   ```bash
   uv sync
   ```

3. Open the [course website](https://rebp.github.io/python-for-ts-devs/) or
   double-click `index.html` to read locally. Start from the curriculum or
   use **Find a lesson** to search by lesson number, title, or topic heading
   (try `8.1`, `keyword-only` or `enum members`). On smaller screens,
   tap the menu icon to open **Lessons** and find the search box. Use the
   sun or moon icon to switch themes. You can swipe sideways inside wide
   diagrams and code examples.

4. Start the exercises:

   ```bash
   uv run course.py
   ```

   It shows your first exercise and runs its tests. They fail, because you
   haven't written anything yet. That's expected.

## How to take the course

For each lesson:

1. **Read the lesson** in the browser. Start with the quick comparison, then
   work through the examples before practice.
2. **Do its three exercises** with `uv run course.py`, which always shows the
   next one.
3. **Compare with the solution** in `solutions/` once your tests pass, or
   when you're stuck.

The lessons build on each other, so go in order the first time. Lesson 5.2
explains uv properly; until then, `uv sync` and `uv run` are all you need.
Use **Jump to practice** in a lesson to go straight to its exercises. The
website remembers the last lesson you opened and your checkmarks in that
browser. The exercise runner tracks its progress separately.

## How the exercises work

1. `uv run course.py` shows the current exercise: the lesson, the file to edit
   and the task.
2. Open that file. The task is in the docstring of the function or class you
   have to write. Usually the body is just `raise NotImplementedError`, but some
   exercises start from buggy code to fix, or ask you to write tests instead.
3. Write your code, then run `uv run course.py` again. It runs the tests and
   shows any failures. When they all pass, the exercise is marked done and the
   next one appears.

Some exercises can't be checked by a test: predicting output, playing in the
REPL, setting up tools. Those are Markdown files (`ex05_1_predict_append.md`
and so on). Read the instructions, do the task, then mark it done:

```bash
uv run course.py --done
```

(When you run `uv run course.py` in a terminal, it also asks you directly.)

### Commands

| Command | What it does |
| --- | --- |
| `uv run course.py` | Show the next exercise and run its tests |
| `uv run course.py 1.3-2` | Check one specific exercise (any order) |
| `uv run course.py --done` | Mark the current README exercise as done |
| `uv run course.py --list` | List all exercises: ✓ done, ▶ next, · to do |
| `uv run course.py --progress` | Progress bars, overall and per section |
| `uv run course.py --reset` | Forget your progress (your code isn't touched) |

Your exercise progress lives in `progress.json` in this folder. It's in
`.gitignore`, so it stays on your machine. The "Done" checkboxes in the web
page are separate: the browser remembers them, and they don't sync with
`course.py`. Exercise numbers combine the topic, lesson and task: `1.3-2` is
the second exercise in lesson 1.3. Earlier exercise IDs such as `03-2` and
old lesson links still work, and existing progress is retained. Existing
exercise filenames and some comments keep their original IDs so updating the
course does not rename files you may have edited.

## Keeping your copy up to date

The course gets fixes and new lessons. Your solutions live in the same files
you got from Git, so commit your work before you pull, on a branch of your own:

```bash
git switch -c my-work      # once, before you start
git add -A
git commit -m "My progress"
git pull origin main       # get course updates
uv sync                    # in case the dependencies changed
```

If an update changes an exercise you've already solved, Git shows a merge
conflict in that file. Keep your version. `progress.json` is never touched.

## What's in the folder

```text
course.py                 the exercise runner
index.html                the course itself
exercises/
  03-functions/
    ex03_2_average.py         ← you edit this: a stub with the task as its docstring
    test_ex03_2_average.py    ← the tests (no need to touch these)
  05-names-and-objects/
    ex05_1_predict_append.md  ← a README exercise you check yourself
  ...
solutions/                same layout, with reference solutions and README answers
conftest.py, course_helpers.py   test plumbing you can ignore
```

A few lessons are shaped differently:

- **3.6 Typing in depth** also runs `mypy --strict` on your code, so your
  type hints are checked, not just the behaviour.
- **5.1 Modules and imports** is a real package: you edit `shop/pricing.py`,
  `shop/__init__.py` and `main.py`.
- **5.2 and 5.3** (uv, ruff, mypy) are hands-on tooling tasks, done in a scratch
  project, so they're all README exercises.
- **6.1 Testing with pytest**, **6.2-1**, **6.2-2** and **10.1-3** turn it around:
  *you* write the tests. They're checked by running your tests against working
  code (they must pass) and against deliberately broken versions (they must
  fail).
- The later topics go past the language: choosing a web
  framework, structuring and shipping a FastAPI service, command-line tools with
  Typer, and data work with pandas. **11.1-3** builds a Docker image and a
  TypeScript client, so it needs Docker and Node.js. **13.1** has
  open-ended projects instead of tests.

## Tips

- **Run the tests yourself** if you prefer plain pytest:

  ```bash
  uv run pytest exercises/03-functions
  ```

  `uv run pytest` with no path runs everything, which mostly fails until
  you've done the exercises.

- **Try your code in the REPL.** From a lesson folder,
  `uv run python` and then `from ex03_2_average import average`.
- **Editor setup:** point VS Code (or your editor) at the project's Python,
  `.venv/bin/python` on macOS and Linux or `.venv\Scripts\python.exe` on
  Windows, so it finds pytest, Pydantic, FastAPI, Typer, pandas and the rest.
  The Python and Ruff extensions give you the closest thing to the TypeScript
  language server.
- **Stuck?** Each exercise's reference solution is in `solutions/` under the
  same path. Try for a while first, then compare. There's often more than one
  good answer: the tests check behaviour, and only occasionally the technique
  the lesson is about (for example, that you used a comprehension or `yield`).
- **Lint your code** the way lesson 5.3 teaches: `uv run ruff check exercises`.

## Troubleshooting

- **`uv: command not found`** (or "not recognized" on Windows) right after
  installing uv: open a new terminal so it picks up the updated `PATH`.
- **VS Code underlines every import in red**: it's using a different Python.
  Run "Python: Select Interpreter" from the command palette and pick the one in
  `.venv`.
- **`ModuleNotFoundError: No module named 'fastapi'`** (or pytest, pandas…):
  you ran plain `python` or `pytest`, which can't see the project's
  libraries. Put `uv run` in front: `uv run python …`, `uv run pytest …`.
- **An exercise you've solved shows as not done**: run
  `uv run course.py <id>`, for example `uv run course.py 1.3-2`. It marks the
  exercise done as soon as its tests pass.

## For course maintainers

The tests import exercise modules by name (`from ex03_2_average import average`).
`pytest --solutions` runs the same tests against `solutions/` instead, through
an import hook in `conftest.py`:

```bash
uv run pytest --solutions
```

```bash
uv run course.py --verify
```

`--verify` checks the whole pack: every tested exercise must fail on its stub
in `exercises/` and pass on its solution, and every README exercise must have
an answer in `solutions/`. Run it on a fresh copy, since solved exercises in
`exercises/` count as "not failing".

The same checks run automatically on Linux, macOS and Windows on every push
(`.github/workflows/ci.yml`). If one of them fails, the course is broken for
someone, so fix it before sharing.
