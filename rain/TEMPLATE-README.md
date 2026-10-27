# rain — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@rain @ f22e5686743c0bd455ef7eb549e4ac694998ba4f

## What this is
Contestant-facing starter templates: `rain_template.py/.cpp/.java` in
`templates/`. Problem: n drones in 3D space, each with a rain bucket and a
fixed cardinal 1-unit/day movement; drones directly under another collect no
rain that night; total rain over k nights. Output: one integer.

## ⚠️ STATUS: PARTIAL — the branch is a STUB
calico-fa26@rain f22e5686 `rain/main.py` is byte-identical to the example
`add` problem (Problem name still `add_test_fa25`, seed `add_seed_600`,
`TestCase(X, Y)` addition generator), and `rain/submissions/accepted/sol.cpp`
is the example addition solution. **The actual rain problem is not yet
implemented in the branch** (10-25 commit "Rain branch" = folder copy).
Per task rules I did NOT invent requirements: I templated the parts that ARE
grounded (the thread's I/O description + the author's in-thread solution
draft) and left `solve()` empty.

## What the template implements
- `solve(N, X, Y, Z, DIR, K) -> int/long` (parallel arrays per drone: start
  x, y, z, direction string 'N'/'E' (N/E only — author-final 23:03Z); K nights). `# YOUR CODE HERE`,
  default `return -1`.
- `main()`: T, then per case `N K` line + N lines of `X Y Z DIR`.
- C++/Java use `long long`/`long` for K and the return (k ≤ 1e9, n ≤ 1e5 →
  total up to ~1e14, exceeds int). This deviates from the "prefer int for
  main set" rule on purpose: the answer provably doesn't fit int; the
  author's own in-thread C++ uses `ll ret = k * n`.

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`
  (int-preference rule + its "if the main test set requires long, use long"
  exception).
- I/O contract: NOT from the branch (stub). From the thread — see below.
  The author's in-thread C++ solution draft (msg 1563763159574118533) reads
  exactly: `cin >> n >> k;` then per drone `cin >> x >> y >> z >> d` (char),
  which I mirrored.

## pw-thread context (internal — do not ship)
- Thread id 1562287342704791583 (rebuild of OLD Drone Rain 1558726992239792158,
  which is Dead/superseded).
- Opener (1562287342704791583): n ≤ 1e5 drones, 1 unit/night, cardinal move,
  shielding rule, k ≤ 1e9 nights; guarantees: no drone under another
  initially, no head-on collisions.
- ✅ RESOLVED (author, randomchicken 2026-10-26 23:03Z): **N/E only.**
  Template docstring narrowed to {N, E} (code unchanged — the template
  never validated directions). Franklin re-verified compile+run.
- PENDING author confirmation: guarantee wording. Author delegated the
  choice to Franklin (23:04Z "up to you… whichever seems easier for
  people to understand"). Franklin's recommendation posted in-thread
  (msg 1564430071593435147, 00:06Z): **"no drones start over each
  other"** — stricter, more intuitive, and any valid input satisfies the
  looser "no same (x,y) + same direction" version, so ink's O(n log n)
  draft stays correct. Awaiting ryan/author confirmation before the
  statement locks; the template is unaffected either way (statement-only
  wording).

## Verification performed
- py_compile + run on a hand-built sample (3 drones, k=5, N/E mix): rc=0,
  prints -1.
- g++ -std=c++17 -O2 compile + run: rc=0, -1.
- javac 17 + `java -cp dir Solution`: rc=0, -1.
- All three parse the full input with no errors. Sample was hand-built (no
  sample data exists in the stub branch) — it matches the thread format and
  the author's solution draft, not any in-repo fixture.

## Open questions / what a human should double-check
1. **The branch must be rewritten before ANY of this ships** — main.py,
   generator, validator, and sol all need to become the real rain problem.
   Once main.py exists, re-derive the template I/O from its
   `write_test_in` and regenerate samples.
2. Directions: **RESOLVED — N/E only** (author 23:03Z); docstring narrowed.
   Guarantee wording: PENDING (Franklin rec posted 00:06Z, msg
   1564430071593435147) — statement-only, no template change.
3. Coordinate bounds (|x|,|y|,|z|) and T/case counts are NOT stated anywhere
   I can see (thread says only n ≤ 1e5, k ≤ 1e9). The statement draft may
   exist only on Overleaf. Don't ship until bounds are known.
4. Direction token format: single char 'N' (thread + author draft) vs word
   "north" — the statement must pin this down; template assumes a single
   whitespace-separated token either way.
5. Output scale: one integer, may exceed 2^31 (use 64-bit) — flag to the
   judge-host team if per-language limits make this a problem (PyPy/Java
   fine; C++ contestants must use long long — the template models that).
