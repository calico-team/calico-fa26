# verity — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@verity @ 1deaafacfa000fa785c9c2bd92522a83153272cc

## What this is
Contestant-facing starter templates for an INTERACTIVE problem:
`verity_template.py/.cpp/.java` in `templates/`. "Big Ben's first
interactive": guess a hidden string of length N over an alphabet of K chars;
each guess is a full string of length N; the judge replies either
"CORRECT" or a length-N string where confirmed-correct positions show the
true char and wrong positions show "_".

## What the template implements
- A `submit(GUESS)` helper (python: `print(..., flush=True)` + `input()`;
  C++: `cout << ... << flush` + `cin >>`; Java: `out.println` + `out.flush`
  + `in.readLine()`) that sends one guess and returns the judge reply. This
  is the interactive-template convention mandated in-thread (dylan 10-24,
  msg 1563433839362310195: "in template, should provide some 'submit'
  function which takes in a guess and returns the next input from judge").
- `solve(N, K, A)` with docstring + `# YOUR CODE HERE`, empty body — the
  contestant writes their query strategy inside it.
- `main()`: T, then per case `N K` line + alphabet line (K single-char
  tokens). Matches the branch's accepted sol and the interactor exactly.
- The template does NOT auto-loop a naive strategy (e.g. fill with A[0]) —
  an empty body is the faithful "starter"; a wrong-but-running default would
  burn the guess budget and mislead.

## I/O protocol (verified against the branch's REAL interactor)
Protocol source: calico-fa26@verity 1deaafac `executables/run.py`:
- Program reads T, then per case reads `N K` and the K-char alphabet line.
- Program writes full-guess strings; interactor replies with "CORRECT" or a
  reveal string (correct pos = true char, else "_").
- Interactor WA's on: >100 guesses (msg "Exceeded maximum number of allowed
  guesses"), wrong-length guess, or a char outside the alphabet.
- Note the guess budget: the interactor hard-limits 100 guesses total per
  case (not the "≤2N" that the thread's rank notes imply). The template
  docstring says "use no more than 2*N guesses" per the thread framing —
  **verify the final statement says 100 or 2N, and keep template text and
  interactor limit consistent** (if N can exceed 50, 2N > 100 and the
  interactor will WA a "correct" 2N-strategy; the accepted sol loops K times
  over positions, i.e. up to K*N guesses... which would ALSO exceed 100 for
  N*K > 100. See open question 1 — the guess budget looks inconsistent in
  the branch.)

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`
  (solve + docstring + marker + main I/O). For interactive problems the
  in-thread submit() convention (above) extends the spec.
- I/O contract: `verity/main.py` `write_test_in` (T; per case `N K` line +
  alphabet line) and `executables/run.py` (reply semantics). Accepted sol
  `verity/submissions/accepted/verity.cpp` and RTE `verity.py` both use the
  same read shape — triple-confirmed.
- Java: static BufferedReader/PrintWriter per pw-kb java-templates R3; the
  static handles are declared at class top (before submit/solve) so both
  can use them.

## pw-thread context (internal — do not ship)
- Thread id 1554687891823927296. Query format decided 10-05 (bread8483,
  msg 1556816613108482159) — NOTE: that in-thread format was `?i T` (index +
  type char), but the BRANCH's shipped interactor uses full-string guesses
  with positional reveal. The branch protocol (full-string) is what the
  template implements; the thread's `?i T` format is superseded. If the
  final statement still describes `?i T` queries, the whole template (and
  interactor) is wrong — flag loudly.
- Rank 1 interactive (mattyl37, msg 1554710693620482069); "babys first
  interactive" milestone framing (msg 1556848280321789983).
- The string's structural constraints (L needs V within 1–3 spaces, C needs
  F within 1–2, V/C not adjacent, no char repeats, every 6 chars contains
  C/F/L/a — per pw-kb verity.md from msg 1556816613108482159) are
  ANSWER-relevant and intentionally NOT in the template docstring (the
  template only says "guess the hidden string").
- Interactor status: "broken" 10-18 → "testing ready" 10-19 (branch tip
  commit "testing ready").

## Verification performed
- All three templates compile (py_compile / g++ -std=c++17 -O2 / javac 17)
  and run their main() to EOF on a minimal interactive-style input.
- All three run against the branch's REAL interactor (executables/run.py,
  test input `1\n4 4\nL C F V`): clean exit, interactor WA exit 43
  ("Solution exited before completing the interaction") — i.e. the protocol
  handshake (T, N K, alphabet, guess/reply) is correct end-to-end; an empty
  template correctly produces a clean WA rather than a hang or crash.
- Positive end-to-end proof: a throwaway oracle using the EXACT template
  submit()/main() shape (candidate-elimination) ran against the real
  interactor on `2\n5 3\nL C F\n8 4\nA B C D` → interactor exit 42 (AC).
  The template's plumbing is sufficient for a correct strategy to win.

## Open questions / what a human should double-check
1. **Guess budget inconsistency:** interactor hard-limits 100 guesses/case;
   the thread frames it as "≤2N queries"; the accepted sol can use up to
   K*N. With T up to 100 cases and N up to 100 (main.py generator), 100
   total per case is only ever satisfiable when N ≤ 50 and strategy is
   tight. Reconcile: (a) interactor limit, (b) statement wording, (c)
   template docstring — they must agree. If the statement says 2N and N>50
   is possible, the interactor's `num_guesses > 100` check WA's valid
   solutions.
2. **Query format: full-string guess (branch) vs `?i T` (thread 10-05)?**
   Template + interactor agree on full-string; the 10-05 thread message
   says otherwise. Confirm the statement matches the branch (full-string).
3. Statement is on Overleaf (not in repo) — the structural constraints
   (what makes a valid hidden string) aren't in the repo at all. Template
   deliberately stays agnostic to them; nothing to check here beyond not
   leaking them.
4. `executables/run.py` reads the alphabet line as space-separated single
   chars; sample test case 2 uses 5 chars "A B C D E" with K=5 — fine. But
   main.py's sample `TestCase(10, 5, ['A','B','C','D','E'])` has N=10,
   K=5 while case 1 is N=4, K=4 — the interactor's 100-guess cap is fine
   for these.
5. Interactive judging on the judge (runpipe wiring, `executables/run`
   shell script paths) is the host team's concern — templates don't touch
   it, but the `run` script's `sudo`-arg skipping and runpipe lookup were
   hand-rolled; a judge-host dry run of the zip is still the real test.
6. The branch also carries WA `wa.cpp` (an addition solution, clearly
   copy-paste leftover — its docstring even says it's from spring 2023) and
   RTE `verity.py` — irrelevant to templates, but wa.cpp is not a valid
   interactive submission (would be a useful IE/CE test instead); flagged
   for the writer's awareness.
