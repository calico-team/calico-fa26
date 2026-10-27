# forgor — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@forgor @ 0688bbadd11ac765d84d8c784b988b3511204c4a

## What this is
Contestant-facing starter templates: `forgor_template.py/.cpp/.java` in
`templates/`. Problem "Big Ben Forgor": two-phase tree-erasure problem.
Big Ben writes one integer a_i (≤ 2e6) beside each vertex of an N-vertex tree
(2 ≤ N ≤ 1024); one a_i is erased (replaced with -1); the contestant's
program must run once in each phase (per the statement, pinned 2026-10-26):
- Phase 1 input: N + the parent array P_1..P_N (P_i = i for the root) →
  output one line a_1..a_N (your encoding).
- Phase 2 input: N + the a_i's (one is -1, your own phase-1 output) →
  output one line P_1..P_N (the original parent array).
Phases run as separate program invocations; nothing persists except the
a_i's.

## ✅ STATUS: CANONICAL FORMAT PINNED 2026-10-26 (Overleaf statement first
## draft, shown by dylan in-thread as screenshot, msg 1564350623468626062)
The statement's "Special Interaction Format" section (verbatim key lines):
- "The first line of the input contains an integer `T` ... as well as
  either `1` or `2`, denoting the current phase." → **T first, then phase.**
- Phase 1 input: `N`, then `N` integers `P_1..P_N` — **the parent array**
  (`P_i = i` for the root), NOT edge lines. Output: one line of `N` ints
  `A_1..A_N` (your encoding).
- Phase 2 input: `N`, then `N` integers `A_i` (your phase-1 output with one
  value replaced by `−1`). Output: **one line of `N` integers
  `P_1..P_N` (parent array)** — not edge lines.
- "Your program will be run twice per test set" — once per phase; the
  phase-2 run always corresponds to the phase-1 run just finished.

This RESOLVES the earlier conflict:
1. T-first + parent-array output **matches the branch's accepted sol**
   (forgor.cpp) — templates were already on the right side there.
2. The thread opener's "P first" + edge-lines output is SUPERSEDED by the
   statement draft (dylan wrote the draft 10-24, msg 1563678472595841195).

**Remaining gap:** the statement's phase-1 INPUT is the parent array — the
first templates shipped here (2026-10-26 17:25) templated phase-1 input as
N-1 edge lines (from the thread opener). All three templates were REWRITTEN
2026-10-26 (~19:30Z) against the statement: both phases now read one line
of N ints and print one line of N ints. main.py is STILL the example stub —
a real generator + validators + the branch sol must all be brought to this
format before anything ships. If the statement draft later changes,
re-derive from it (it is the canonical artifact — contestants read it).

## What the template implements (statement format, pinned 2026-10-26;
## solve-split per author feedback, 2026-10-26 msg 1564356233413140522)
- `solve_phase1(N, P)`: `P` = the parent array exactly as the statement
  defines it (`P[i]` is the parent of vertex i+1, or i+1 if vertex i+1
  is the root). Returns the N ints `A_1..A_N`, your encoding of the tree.
- `solve_phase2(N, A)`: `A` = the N ints `A_1..A_N` as the statement
  defines them (your own phase-1 output for this test case, with exactly
  one value replaced by -1). Returns the N ints `P_1..P_N`, the parent
  array of the original tree.
- `main()`: first line `T` then phase; per case: one line of N ints read
  into the statement's own symbol — `P` in phase 1, `A` in phase 2 — then
  the matching solve_phase* runs and the phase's output symbol (`A` in
  phase 1, `P` in phase 2) is printed as one line of N ints. Every
  variable used is a statement formal variable, per the owner's
  formal-variables convention (ryan, 2026-10-26 #pw-forum: everything
  given to the contestant must be a formal variable — `\var{...}`,
  capital, subscriptable — and templates/solutions must use the exact
  statement symbols for input/output/signatures).
- Spec deviation (flagged): calico-fa26@main create-templates.md says
  "Each template must have a function named `solve(...)`. " The author
  overrode this for forgor in-thread (two phase functions instead of
  one). If the spec is meant to apply, re-merge into a single `solve`
  with a phase parameter and unambiguous names — or ask dylan to update
  the spec. (ALL_CAPS rule satisfied: formal params N, P, A are
  statement symbols as-is.)
- Default returns: N zeros (clearly-wrong placeholder that still parses
  as valid ints so main() doesn't crash).
  (create-templates.md: "Return something clearly and sensibly wrong.")
- Note vs the branch sol: the sol's phase-1 INPUT is N-1 edge lines and its
  encoding uses child COUNT, not the thread's XOR-of-children — the sol is
  one draft behind the statement. It must be rewritten to read the parent
  array and re-AC'd against the new generator before shipping. (The
  committed prebuilt binary `forgor` goes with it.)

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`
  (3 files, solve+docstring+marker+main I/O; int for main-set — N ≤ 1024,
  a_i ≤ 2e6 fit int; phase-2 parent/edge values ≤ 1024 fit int).
- I/O contract (canonical): the statement's "Special Interaction Format"
  section — Overleaf first draft (dylan, 10-24, msg 1563678472595841195),
  shown as a screenshot in-thread 2026-10-26; T then phase on line 1, both
  phases one line of N ints in and out. The branch's accepted sol
  (calico-fa26@forgor 0688bbad `forgor/submissions/accepted/forgor.cpp`)
  agrees on T-first and parent-array output but reads phase-1 input as
  edge lines and encodes child count — one draft behind the statement; see
  open question #3. Note: main.py references `sol.cpp` which does not
  exist; the real accepted files are `forgor.cpp` + a committed prebuilt
  binary `forgor` (the binary should not ship in a contestant zip).
- Historical two-phase precedent (format reference only): calico-sp24@
  a42a06c `amnesia/` (single-input single-output string problem, NOT the
  same two-run structure — dylan's "similar to amnesia?" pointer, msg
  1563678472595841195, was about the erasure concept, not the I/O).

## pw-thread context (internal — do not ship)
- Thread id 1555815239742656613. Opener = the written format (2) above.
- Intended encoding (spoiler): v_i = p_i + 2^10 * (xor of child indices),
  root-at-1; N ≤ 1024 < 2^10 makes the 10-bit parent field work. (msg
  1555815291223539744). The branch's sol instead encodes p_i + 2^10 *
  (CHILD COUNT) — a DIFFERENT (simpler) encoding than the thread's intended
  one. Not template-relevant (the a_i's are opaque to the template), but it
  confirms the branch and thread were written by different drafts and the
  format drift is real.
- "rank 2 feels reasonable" (msg 1557213115681083476).
- Statement first draft done 10-24 (msg 1563678472595841195) — that draft
  presumably pins the canonical format; it's on Overleaf, not in the repo.

## Verification performed (2026-10-26, post-rewrite — all real runs)
- Rewritten templates (both phases: one line of N ints in/out) verified
  with hand-built inputs (stub branch has no forgor sample data):
  - `2 1\n3\n1 1 3\n4\n2 1 1 2` → `0 0 0` then `0 0 0 0` (N=3 and N=4
    parent-array inputs).
  - `2 2\n3\n1025 1025 -1\n4\n1027 1027 -1 1030` → `0 0 0` then
    `0 0 0 0`.
- python3: rc=0, both runs.
- g++ -std=c++17 -O2 compile + run: rc=0, identical output.
- javac 17 (Temurin 17.0.21, /opt/data/cache/scratch/fa26/) +
  `java -cp dir Solution`: rc=0, identical output.
- All three parse the full two-case input with no errors.
- Post solve-split re-run (2026-10-26, ~19:55Z): same two inputs, all
  three languages, 6/6 runs rc=0, identical output (`0 0 0` / `0 0 0 0`).
- Post formal-variables re-run (2026-10-26, ~20:05Z): main() now reads
  into `P`/`A` per phase (owner's formal-variables convention); same two
  inputs, 6/6 runs rc=0, identical output.
- javac 21 (Temurin 21.0.13, /opt/data/cache/scratch/fa26/) — dylan
  confirmed the judge is on javac 21 (2026-10-26): forgor_template.java
  compiles + runs both phases rc=0, identical output. (The 17.0.21
  results above remain valid; 21 is the authoritative target.)
- Judge-conformance re-run (2026-10-26, calicoguide.pdf canonical table —
  ryan msg 1564397842871754792):
  - C++: `g++-13 13.3.0 -x c++ -Wall -O2 -static -pipe` (exact DOMjudge
    8.3.1 cpp/run flags): compiles, 0 warnings; static binary runs both
    phases rc=0.
  - Python: CPython 3.12.13 (judge: 3.12.3): both phases rc=0.
  - Java: javac 21.0.13 (judge: OpenJDK 21.0.10): both phases rc=0.
  - Full table: /opt/data/pw-kb/conventions/language-versions.md.

## Open questions / what a human should double-check
1. ~~Canonical input format: branch-sol (T P first line) vs thread (P first
   line)?~~ **RESOLVED 2026-10-26: T first, then phase (statement draft,
   dylan's screenshot in-thread, msg 1564350623468626062).**
2. ~~Phase-2 output: edge lines (thread) vs parent array (branch sol)?~~
   **RESOLVED: parent array, one line of N ints (statement draft).**
3. **main.py is the example stub** — no generator, no validators, no sample
   data for forgor. The generator (write_test_in), validators, branch sol,
   and the committed prebuilt binary `forgor/submissions/accepted/forgor`
   all still encode the old draft (edge-line phase-1 input, child-count
   encoding) and must be rewritten to the statement format before anything
   ships.
4. The statement screenshot has NO constraints section — T and N bounds
   (thread says N ≤ 1024; encoding bound a_i ≤ 2e6) should appear in the
   final statement.
5. Confirm the judge drives the program as the statement says ("run twice
   per test set"): two invocations per test set, phase flag on line 1.
