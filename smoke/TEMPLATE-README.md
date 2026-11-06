# smoke — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-11-06 · Author: Franklin · Base: calico-fa26@smoke @ 866fca8
("templates and rank 1 sols that hopefully work", Dylan 2026-10-27)

## What this commit does
The base branch already ships `smoke/templates/smoke_template.{cpp,java,py}`.
This commit completes them to the template spec and adds the checker:

- **cpp**: author's file kept as-is (signature, doc-comment, tabs) — only adds
  the required `// YOUR CODE HERE` marker inside `solve()` + trailing newline.
- **java**: author's file, indentation normalized (it mixed tabs/spaces);
  adds `// YOUR CODE HERE` marker.
- **py**: author's file normalized to PEP8 (4-space indent, two blank lines
  between defs); adds `# YOUR CODE HERE` marker. Signature, docstring, and
  I/O logic unchanged.
- **scripts/check_templates**: new, per `.claude/commands/create-templates.md`
  on main. Runs from `smoke/`: compiles + runs each template on
  `data/sample/00_main.in`, checks the stub prints one empty line per case,
  then injects a `N R A[0] A[-1]` echo at the marker and checks parsing.
  Honors `PY_CMD` / `CPP_CC` / `JAVA_CMD` / `JAVAC_CMD` env overrides. Cleans
  up binaries/classes.

Stub return is `""` (matches the branch's existing shape; the answer is a
YES/NO string). `int` for N/R/A per main-set constraints (validator: N,R ≤
1000, a_i ≤ 10000) — no long needed anywhere.

## Convention sources
- CALICOmpendium v2.1, "Test Cases, Validators, and Templates" tab (verified
  Sep 7, 2026): 3 languages per problem; `<problem name>_template.<ext>`;
  solve called per test case, main prints its return; comment above solve for
  C++/Java, inside for Python; Java class `Solution` + BufferedReader/PrintWriter.
- calico-fa26@main `.claude/commands/create-templates.md`: `solve(...)` +
  docstring + `# YOUR CODE HERE` + `main()` I/O; ALL_CAPS vars matching
  statement formal names; PEP8; int-preference rule; check_templates script.
- sp26 references used as shape precedent: `mycelium/scripts/check_templates`
  (stub+params check pattern) and sp26 `laser`/`files` templates.

## Verification (all real runs, 2026-11-06)
Sample data: `data/sample/00_main.in` reproduced byte-for-byte from main.py's
`add_sample_test` via `TestFile.write_test_in` (trailing spaces included;
data/ is gitignored — regenerate with `python main.py` if needed).
Expected answers from the branch's own accepted sol: YES NO YES NO.

- `./scripts/check_templates`: 6/6 PASS (stub + params × py/cpp/java).
- C++ judge flags (`g++-13` 13.3, `-x c++ -Wall -O2 -static -pipe`): compiles,
  0 warnings; stub prints exactly 4 newlines.
- Java judge toolchain (javac/java 21, Temurin 21.0.13): compiles, runs clean.
- Python 3.13 `py_compile` OK; stub + params run OK.
- Cross-check: branch `scripts/validator_main.py` accepts the sample input and
  an N=1 edge case; template I/O consumes the validator's format.

## Open notes for the author
- The two stale `add_test_fa25_draft_*.lock` files at `smoke/` root are
  unchanged (drop-before-zip is an author/ryan call).
- If the statement renames the formal input variables, the template params
  must follow (ALL_CAPS-match rule).
