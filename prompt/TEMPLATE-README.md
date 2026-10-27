# prompt — TEMPLATE-README (internal, reviewer-facing)

Date: 2026-10-26 · Author: Franklin (task #51) · Branch: calico-fa26@prompt @ 22a258d54b1fa940daf15e98669acceb48d77e42

## What this is
Contestant-facing starter templates: `prompt_template.py/.cpp/.java` in
`templates/`. Problem: given a prompt string S (tokens use underscores instead
of spaces), output S with one appended keyword-dependent sentence. Rank 1.

## What the template implements
- `solve(S: str) -> str` with docstring, `# YOUR CODE HERE`, default
  `return ""`. `main()`: read T, then one whole-line S per case,
  `print(solve(S))`.
- C++/Java mirror the same single-arg string solve.

## Convention sources (repo evidence)
- Template spec: calico-fa26@main a776651 `.claude/commands/create-templates.md`.
- I/O contract: calico-fa26@prompt 22a258d5 `prompt/main.py`
  `TestFile.write_test_in` — T, then one line per case containing S. Accepted
  solutions `prompt/submissions/accepted/prompt.{cpp,py}` read S with
  `cin >> S` / `input()` (single token, no spaces in S).
- Reference shape: calico-fa25@01b74071 `bizzfuzz/templates/bizzfuzz.{cpp,java,py}`
  (clean 3-language string-solve reference per pw-kb conventions P1).

## pw-thread context (internal — do not ship)
- Thread id 1562281914080174110. "spaces→underscores so cpp doesn't need
  getline" (dylan 10-21, msg 1562314655295348787) — this is WHY S is a single
  token; the template must read S as one token/line, NOT parse spaces.
  My templates do that.
- "should be testing ready now" (dylan 10-21, msg 1562314690053406761).
- The four keyword→sentence mapping is a solution detail, deliberately NOT
  in the template (template returns empty; the docstring only says
  "append the appropriate sentence").

## Verification performed
- py_compile + run on branch sample (from prompt/main.py): rc=0, 4 empty lines.
- g++ -std=c++17 -O2 compile + run: rc=0, 4 empty lines.
- javac 17 + `java -cp dir Solution`: rc=0, 4 empty lines.
- All consume the full sample (5 underscored strings) with no parse errors.

## Open questions / what a human should double-check
1. The exact appended sentences and the keyword priority (write_me / what_is /
   solve / else) are the ANSWER — do NOT leak them into the template docstring
   or any shipped text. Current docstring is neutral ("the appropriate
   sentence"). Confirm the statement on Overleaf matches this framing.
2. Does S contain only `[a-z0-9_]`? main.py generator uses
   `ascii_lowercase + digits + '_'`. Template treats S as an opaque token —
   fine either way, but confirm no uppercase/other chars sneak in.
3. Single rank (main only, rank=1). No bonus — no long-variant concern.
4. prompt/main.py comment header is the stale example text — cosmetic.
