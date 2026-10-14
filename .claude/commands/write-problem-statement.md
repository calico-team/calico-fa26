# Write Problem Statement

Write and revise the problem statement `.tex` file for a CALICO problem.

## File structure

The tex file lives at `[problem]/[problem].tex`. This is a temporary working copy — the live version is on Overleaf. It uses custom LaTeX commands:

```latex
\renewcommand{\problemname}{Display Name}
\renewcommand{\problempoints}{X+X+X+X}    % one X per test set
\renewcommand{\problemrank}{2+3+3+4}      % rank per test set
\renewcommand{\problemid}{problem_id}
\renewcommand{\problempages}{4}
```

Sections in order: Introduction, Problem Statement, Input Format, Output Format, Constraints, Sample Test Cases, Sample Explanations.

## Points and rank

- `\problempoints` uses `X+X+X+X` format with one entry per test set (main + bonuses). Actual point values are assigned later.
- `\problemrank` uses the same `+` notation. Ranks come from the `Subproblem` definitions in `main.py`. Rank 2 = general high school CS, rank 3 = intermediate, rank 4 = advanced.

## Problem statement principles

Crafting a problem statement is an incredibly precise task that is both artistic and technical. It requires balancing clarity, conciseness, technical accuracy, and game design.

### Audience awareness
- The lowest applicable rank determines the baseline reading level. Rank 2 targets general high school CS students — avoid advanced terminology like "Manhattan distance" or "cardinal neighbors" when simpler phrasing works.
- Consider how speed-readers, ESL contestants, and first-time competitors may misinterpret phrasing.
- Consider multiple interpretations of every sentence. If an alternative reading produces a different problem, the wording must be tightened.

### Conciseness over completeness
- Every sentence must earn its place. If a fact is implied by the rules, don't state it separately.
- Prefer restructuring to adding clarifying sentences. For example, using "converts empty tiles into X" implies permanence without needing "once a tile is claimed, it stays forever."
- When two rules share structure, decide deliberately whether to repeat (for scannability) or back-reference (for brevity). Full parallel repetition is preferred when the only difference is a number.

### Deliberate information control
- Problem statements are a form of game design. What you *don't* reveal is as important as what you do.
- If a key insight (e.g., "the answer is always finite," "the region is always convex") is something contestants should deduce, do not state it. Frame the question to be correct without revealing the insight. Example: "Find the total number of tiles mycelium will ever occupy" is carefully worded to avoid revealing that mycelium always gets surrounded.
- Sample explanations may reveal more since the contestant already has the answer, but still avoid giving away the core algorithmic insight.

### Terminology consistency
- Establish terms early and use them consistently throughout. For example, if the grid has "tiles," never call them "cells" or "squares." If time is measured in "ticks," never say "steps" or "rounds."
- Define terms implicitly through usage rather than explicit definitions when possible. "All other tiles are empty" defines "empty" through context.
- Terms that don't need formal definition: common words whose meaning is clear from context (e.g., "occupy," "spread"). Only define terms that have domain-specific or ambiguous meanings.

### Structural patterns
- Use bullet points or `\begin{itemize}` for parallel rules that share a structure but differ in parameters. This makes differences visually scannable.
- Use `\begin{enumerate}` only when order matters (sequential steps within a tick).
- One anchor sentence before diving into mechanics helps frame the model. Example: "Time progresses in discrete ticks:" followed by bullet rules.

### Verb choice
- Prefer tile-as-subject ("empty tiles become grass") over agent-as-subject ("grass converts tiles") — it reads more naturally and avoids implying agency.
- Be consistent with one verb for the core action throughout (e.g., "becomes" everywhere, not "becomes" in one place and "converts" in another).
- The conflict resolution sentence can use different phrasing for emphasis ("grass wins" is acceptable informal shorthand at rank 2).

## Input format

- First line: always `$\var{T}$` with "denoting the number of test cases that follow."
- Use "denoting" as the standard verb for describing what variables represent.
- If a test case is a single line, describe it directly without bullet points. Use bullets only for multi-line test cases.
- Variable names in `$\var{...}$` with subscripts as natural LaTeX: `$\var{X_G}$` not `$\var{X\_G}$`.
- When variables appear space-separated on one line, list them without commas in the `$\var{...}$` sequence, since they are literally space-separated in the input: `$\var{X_G}$ $\var{Y_G}$ $\var{X_M}$ $\var{Y_M}$`.

## Output format

- Mirror the phrasing used in the problem statement's closing question. If the statement says "Find the total number of tiles that mycelium will ever occupy," the output format says "output a single integer denoting the total number of tiles that mycelium will ever occupy."

## Constraints

- Common constraints across all test sets first, then per-set subsections.
- Use `-X \leq \var{...} \leq X` format (symmetric bounds) for readability rather than `|\var{...}| \leq X`.
- Distinctness constraints use tuple notation: `$(\var{X_G}, \var{Y_G}) \neq (\var{X_M}, \var{Y_M})$`.
- Threshold values must match `constants.py` exactly.

## Sample test cases

- Formatting uses alternating `white` and `gray!12` `\begin{samples}` blocks.
- Input starts with a white block (the T line), then alternates. Output starts with a gray block.
- Numbers must match the generated `data/sample/00_main.in` and `00_main.ans` exactly. Never hand-write sample data — always pull from the generated files.
- Download links follow the pattern: `https://calico.cs.berkeley.edu/files/calico-sp26/contest/[problem]/data/sample/00_main.{in,ans}`

## Sample explanations

- Explain a few representative cases, not necessarily all. Pick cases that illustrate different behaviors (minimal case, moderate case, large case).
- Okay to reveal that a region gets enclosed or bounded in explanations, since the contestant already has the answer.
- Avoid referencing advanced concepts not introduced in the problem statement (e.g., don't say "Manhattan distance" if the statement never uses that term).
- Use `$\mathbf{N}$` for the answer value in each explanation.

## Image placeholders

- Use LaTeX comments: `% [IMAGE PLACEHOLDER: description of what the image should show]`
- Good places for images: after the problem statement rules (showing progression over time), in sample explanations (showing specific test case states).
- Be specific about what the image should and should NOT reveal (e.g., "final state explicitly NOT showing mycelium fully enclosed by grass" to avoid giving away the insight).

## Workflow

1. Start from the existing tex or create the skeleton with all sections.
2. Draft the problem statement — iterate on wording carefully. Think about multiple interpretations.
3. Fill in input/output format, constraints (from `constants.py`), and samples (from generated data).
4. Write sample explanations for representative cases.
5. Add image placeholders where visuals would help.
6. The tex file is a working copy — the live version is on Overleaf. Edits here are for drafting and review.
