# Create Templates

Create contestant templates and a template checker script for a CALICO problem.

## Templates to create

Create three files in `[problem]/templates/`:
- `[problem]_template.py`
- `[problem]_template.cpp`
- `[problem]_template.java`

Each template has a `solve(...)` function with a docstring and `# YOUR CODE HERE`, plus a `main()` that handles I/O.

### Conventions
- Input variable names: CAPITALIZED ALL_CAPS (e.g. `X_G`, `Y_G`, `N`)
- Docstring: one param per line with description
- C++ / Java: use `int` for main test set constraints (not `long long`/`long`)
- Python: PEP8 — two blank lines between function defs and before `if __name__ == '__main__':`
- Java: use `BufferedReader` + `PrintWriter` (see existing templates for boilerplate)

## check_templates script

Create `[problem]/scripts/check_templates` (bash, executable). It should:
- Be run from the problem directory: `./scripts/check_templates`
- Use `PY_CMD` (default `python3`), `CPP_CC` (default `g++`), `JAVA_CMD` (default `java`) env vars
- For each template: compile (if needed), run on `data/sample/00_main.in`, compare output to expected
- Print `PASS`/`FAIL` per template with expected vs got on failure
- Clean up compiled binaries after running
- Java: compile with `javac -d scripts/`, run with `java -cp scripts Solution`

The expected output is whatever `solve()` returns as a stub (e.g. four lines of `-1` for 4 sample cases).
