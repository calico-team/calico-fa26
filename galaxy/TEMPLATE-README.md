# galaxy — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@galaxy @ 9bbc29ab591aacd1d0d39f239a3082d666ec4852

## What this is
Contestant-facing starter templates: `galaxy_template.py/.cpp/.java` in
`templates/`. Problem: n×m grid of normal/red/blue tiles; Ben walks
top-left → bottom-right; a button inverts all colored tiles.

## What the template implements
- `solve(N, M, G) -> str` (G = list of N row strings), docstring,
  `# YOUR CODE HERE`, default `return ""`.
- `main()`: T, then per case `N M` header + N grid rows. Grid rows read as
  whole lines (`input()` / `cin >> G[j]` / `in.readLine()`) — no splitting,
  rows contain no spaces.

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`.
- I/O contract: calico-fa26@galaxy 9bbc29ab `galaxy/main.py`
  `TestFile.write_test_in` — T; per case `N M`, then N lines each M chars.
  Accepted solutions `galaxy/submissions/accepted/sol.{py,cpp}` read exactly
  this shape (sol.py: `map(int, input().split())` then N×`input()`).
- Variable names N, M, G taken from the branch's own sol.py signature
  (`def solve(N: int, M: int, G: list[str])`).
- Reference shape: calico-fa25@01b74071 bizzfuzz 3-language set.

## pw-thread context (internal — do not ship)
- Thread id 1552027684207333537. Input block `n m` + n rows of `s_ij` ∈
  {'R','B','.'}; `n*m < 10^5`. (opener 1552027684207333537)
- ⚠️ The statement was flagged "HUGE issues… unusuable" 10-24 (ryan feedback,
  msg 1563385207644618815) and a rewrite was in progress. The BUTTON mechanic
  (rank 3: press at most k times) and the bonus (start,end,k) queries were
  still being designed (msg 1554663440721780828). **The branch's current
  main.py only has `Subproblem('main', rank=2)` and the accepted sols solve
  the plain reachability version (treat color-change as a wall) — the
  template matches the SHIPPED sol/main.py, not the fuller in-thread idea.**
  If the button/query variant lands in main.py, the template's solve()
  signature and I/O must be revised.

## Verification performed
- py_compile + run: rc=0 on a 3-case grid input (template prints 3 empty
  strings). NOTE: the branch's own sample test (galaxy/main.py
  `add_sample_test`) is MALFORMED — its third case declares `9 9` but only
  provides 8 rows, so the raw sample input truncates. I verified against a
  corrected 9-row input. (See gaps below.)
- g++ -std=c++17 -O2 compile + run: rc=0.
- javac 17 + `java -cp dir Solution`: rc=0.

## Open questions / what a human should double-check
1. **Branch bug (galaxy/main.py sample test):** third sample case `TestCase(9,9,[...])`
   has only 8 grid rows (one `BRBRBRBRB` line missing vs the other 9x9 row
   count — 9 rows declared, 8 strings listed). Generated `data/sample/00_main.in`
   will be short one row and every correct solution will EOF-error on the
   sample. Fix before zip generation.
2. Statement status (see pw-thread note): confirm with Jaden which mechanic the
   shipped version actually is — plain reachability (current sols) vs button
   variant — before templates are final. Template currently = plain reachability.
3. Bonus subproblem is commented out in main.py (only `main` active) —
   consistent with the sols. Re-check if a bonus set gets added.
4. Leftover `add_test_fa25_draft_*.lock` files in galaxy/ — will pollute the
   zip if not deleted (flagged in my 10-26 branch audit).
5. `int` sizing: n*m < 1e5 — `int` fine everywhere.
