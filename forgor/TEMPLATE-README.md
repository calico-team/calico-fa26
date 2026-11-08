# forgor — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-11-08 · Author: Franklin (asked by dylan, #franklin thread
1569092900397256756) · Base: calico-fa26@forgor @ ca1df5f

## What this PR does
Rewrites the I/O of the three contestant templates
(`forgor/templates/forgor_template.{py,cpp,java}`) to the current statement's
input format. The templates were still on the **stale T+phase format**
(`T phase` on line 1 + a one-line parent array) from the 10-26 statement
draft; the branch has since migrated to the current format
(main.py `write_test_in`, tip checker `output_validator/run`, statement):

- Phase 1 input: the string `FIRST`, then `N`, then `N-1` lines of `u v`
  (edge lines), then output one line of `N` integers `A_1..A_N`.
- Phase 2 input: the string `SECOND`, then `N`, then one line of `N`
  integers `A_1..A_N` (one is `-1`), then output `N-1` lines of `u v`.
- No test-case count `T` — one case per run; the two phases are two
  separate program invocations (multi-pass judging, `validation_passes: 2`).

Also: edge order + orientation. The ask noted edges are **not guaranteed
to come in lexicographically increasing order** — and since ca1df5f the
generators also **randomize each edge's orientation** (50/50 per edge),
and the tip checker compares **undirected edge sets** (each pair sorted
before the set-compare). The templates therefore treat edges as
unordered pairs in both phases:

- `solve_phase1` takes `E` as `(u, v)` pairs in input order — docstring
  says explicitly that `u` is not guaranteed to be the parent of `v`.
- `solve_phase2` returns `(u, v)` pairs, one per output line — docstring
  says the checker compares the set of edges, so order and orientation
  don't matter.

## What was NOT touched
- `solve_phase1`/`solve_phase2` names, the two-function split (per the
  10-26 author feedback), stub bodies (`[0]*N` / `{}` / `new int[N]` /
  `new int[0][2]`), and file names — per branch-committed conventions.
- `main()` structure: read phase string + N, dispatch, print. Phase-1
  output is one space-separated line; phase-2 output is one edge per line.
  (The template's main() does the printing; solve returns the data —
  11-08 meeting convention. Two-phase run-twice problems are the exception
  where the phase is external to solve(): each solve covers exactly one
  phase, and main() dispatches on the `FIRST`/`SECOND` marker.)
- The accepted solution, checker, main.py — out of scope (open items
  below).

## Verification (2026-11-08, real runs, against tip ca1df5f)
- Judge toolchain: g++ 14.2, jdk-21.0.13+9 (the judge's javac 21),
  python3 3.13.
- **Stub behavior (the committed files):** all 3 langs compile and run
  clean on the statement's sample `FIRST`/`SECOND` inputs (rc=0; phase 1
  prints the zero vector, phase 2 prints nothing) AND on a max-bounds
  N=2·10^5 input in both phases (I/O plumbing scales).
- **I/O plumbing oracle diff:** solve bodies swapped for a working
  reference encode/recover (parent + 2·children-parity, rooted at the
  given orientation), `main()` kept byte-identical per language; all 3
  languages byte-identical to each other on 18 trees (sample +
  non-1-rooted trees + 15 random dfs/bfs/Aldous-Broder trees, N up to
  1000) with **shuffled edge order AND randomized orientation** in the
  phase-1 input, and on every single-value erasure of the phase-2 input.
- **Two-pass judge simulation:** the **ca1df5f** checker
  (`output_validator/run` — undirected set compare) run judge-faithfully
  (phase 2 fed `nextpass.in`) with the oracle as the team: 18/18 AC.

## Format contract note (for the reviewer)
With the ca1df5f checker, a contestant's phase-2 output is checked as an
**undirected edge set**: order and per-pair orientation of the output
edges are irrelevant; the multiset of vertex-pairs must equal the
original tree. The template docstrings state this so contestants don't
waste time trying to re-derive the original orientation/order.

## Open items (NOT in this PR — author-side)
1. **The statement is now stale on both edge-order AND edge-orientation.**
   The statement's phase-1 input still says each line is "two
   space-separated integers $p_i$ and $c_i$ ... where vertex $p_i$ is the
   parent of vertex $c_i$. The edges will be provided in
   lexicographically increasing order." — since ca1df5f the generators
   emit random orientation + random order. Phase-2 output clause still
   says "identical to the input that was provided in phase 1" (order +
   orientation), which also contradicts the now-undirected checker.
   Overleaf-side edits needed (human-side; the Overleaf checkout is
   read-only for me).
2. **Tip accepted solution re-roots at vertex 1**
   (`dfs(dfs, 1, -1)` in phase 1). This is FINE for judging — the
   ca1df5f undirected checker doesn't care about orientation — but it
   means the solution's own phase-1 output no longer lines up with the
   statement's `p_i`/`c_i` "parent of" framing; worth a sanity pass
   before data regeneration.
3. `main.py:24` still references `scripts/validator.py` (missing; only
   `validator_main.py` exists) — ca1df5f fixed other main.py bugs but
   left this line.

## Evidence
- Worktree: /opt/data/cache/scratch/wt-forgor-1108 (origin/forgor @
  ca1df5f)
- Verify harness: /opt/data/cache/scratch/forgor-1108/verify_templates.py
  (full output: all checks PASS, run 2026-11-08 against ca1df5f checker)
- Earlier b358add-era repros (superseded by the ca1df5f checker change):
  /opt/data/cache/scratch/forgor-1108/{root_test2.py,harness_tip.py}
