# Exercise 11.3-3: Rehearse a release (answer)

Declare project metadata, a build backend and `[project.scripts]` in
`pyproject.toml`. Build with `uv build`; it creates a wheel and source archive
in `dist/`. After configuring TestPyPI credentials securely, the upload command
is `uv publish --publish-url https://test.pypi.org/legacy/`. The exercise does
not upload anything.
