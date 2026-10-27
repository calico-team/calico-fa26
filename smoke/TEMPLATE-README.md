# smoke — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@smoke @ 838602b8054aff9c29501a3424771d3be56fd7d0

## What this is
Contestant-facing starter templates: `smoke_template.py`, `smoke_template.cpp`,
`smoke_template.java` in `templates/`. Problem: Omen smoke recharge — input
`T`, then per case `N R` + a line of N integers `A`; output YES/NO string.

## What the template implements
- `solve(N, R, A)` with typed params + docstring, `# YOUR CODE HERE`, default
  `return ""` (matches the branch's existing smoke_template.py/java shape).
- `main()` does the T-loop and all I/O; python uses `input()`, C++ uses
  `cin >>`, Java uses static `BufferedReader in` / `PrintWriter out` with
  `split(" ")` per the smoke_template.java precedent in the branch.
- Java class name `Solution` (judge convention; see pw-kb java-templates R1).

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`
  (3 files in `[problem]/templates/`, `solve(...)` + docstring + `# YOUR CODE
  HERE` + `main()` handling I/O; ALL_CAPS input var names; PEP8 python;
  `int` not `long long` for main-set constraints; Java BufferedReader+PrintWriter).
- Existing branch templates (most mature fa26 problem): calico-fa26@smoke
  838602b8 `smoke/templates/smoke_template.{py,java}`. My py/java are the branch
  files upgraded per the spec (typed signatures, docstring, `# YOUR CODE HERE`,
  4-space indent, trailing newline). I/O handling in `main()` is identical.
  The cpp file is new — the branch had no cpp template (pw-kb cpp-templates P4
  notes smoke is the only fa26 problem with templates).
- pw-kb conventions (2026-10-26 verified): conventions/python-templates.md
  R1-R5, conventions/cpp-templates.md R1-R6, conventions/java-templates R1-R6.

## pw-thread context (internal — do not ship)
- Thread id 1550702242263474288. Input shape confirmed by the branch's own
  accepted solution `smoke/submissions/accepted/smoke.py` and by
  smoke_template.java. K-charge variant (dylan 10-13, msgs 1559699908192243753,
  1559705875017502771) is NOT in the current test sets (main.py has only
  `Subproblem('main', rank=1)`) — template matches the shipped format.
- ryan's 10-24 statement feedback (msg 1563376956920299561) is about the
  statement, not the I/O — no template impact.

## Verification performed
- `py_compile` + run on the branch's sample input (from smoke/main.py sample
  test): rc=0, prints 4 empty strings (default return).
- g++ -std=c++17 -O2 compile + run on same sample: rc=0, 4 empty lines.
- javac 17 + `java -cp dir Solution` run: rc=0.
- All three consume the full sample input with no parse errors (proves main()
  I/O matches write_test_in).

## Open questions / what a human should double-check
1. Branch has NO cpp template — confirm shipping a cpp template is wanted
   (judge offers C, C++, Java, Py3, PyPy, Rust per sp26; templates only cover
   the languages the team actually ships — smoke today is py+java only).
2. `int` vs `long long`: main.py generates R up to 100, a_i up to ~1e4 — `int`
   is safe for main; if the K-charge bonus variant ships, re-check bounds.
3. The branch's smoke_template.py/java use tabs (non-PEP8). I normalized to
   4-space per create-templates.md (PEP8). Reviewer: confirm they're ok with
   the style diff vs the writer's committed files.
4. smoke/main.py comment header is still the stale example text ("add problem,
   A<=100 B<=100") — cosmetic, not template-related.
5. `.lock` files (add_test_fa25_draft_*) in the branch root — unrelated, but
   will end up in the zip build if not cleaned (contest.py zips the problem dir).
