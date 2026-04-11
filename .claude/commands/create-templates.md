# Create Templates

Create contestant templates and a template checker script for a CALICO problem.

The purpose of templates is to give novice contestants an easy way to get started without having to worry about I/O or other obscure language internals. Templates should be simple, idiomatic, and easy to read for beginners.

## Templates to create

Create three files in `[problem]/templates/`:
- `[problem]_template.py`
- `[problem]_template.cpp`
- `[problem]_template.java`

Each template must have a function named `solve(...)` with a docstring and `# YOUR CODE HERE`, plus a `main()` that handles I/O.

### Conventions
- Input variable names: CAPITALIZED ALL_CAPS (e.g. `X_G`, `Y_G`, `N`)
    - Must match the formal variable names as given in problem statement
    - Sometimes it might be more practical to reorganize data in a way that isn't given. For example, we might be given 2 arrays `A` and `B` but it might make more semantic sense to create a list of tuples and call it `items` instead depending on the problem. Use best judgement when this is the case and note in the docstring.
- Docstring: a short 1-2 sentence description of the task at hand (e.g. `Return the total number of tiles mycelium will ever occupy.`) and then one param per line with description.
- Return something clearly and sensibly wrong that is meant to be replaced (e.g. -1 is good if the answer should be a positive integer.)
- C++ / Java: when it makes sense to depending on the constraints of the main test set and problem statement, prefer `int` for main test set constraints (not `long long`/`long`). If the main test set requires long though you should use long.
- Python: PEP8 — two blank lines between function defs and before `if __name__ == '__main__':`
- Java: use `BufferedReader` + `PrintWriter` (see existing templates for boilerplate)

## check_templates script

Create `[problem]/scripts/check_templates` (bash, executable). It should:
- Be run from the problem directory: `./scripts/check_templates`
- Use `PY_CMD` (default `python3`), `CPP_CC` (default `g++`), `JAVA_CMD` (default `java`) env vars
- For each template: modify the template function to print out the received parameters (you can hard code line numbers), compile (if needed), run on `data/sample/00_main.in`, check output to see the parameters are parsed as expected, then remove the prints from the template.
- Print `PASS`/`FAIL` per template with expected vs got on failure
- Clean up compiled binaries after running
- Java: compile with `javac -d scripts/`, run with `java -cp scripts Solution`
