# Design I/O Format

Brainstorm or review the input/output format for a CALICO problem. Call out anything that breaks convention.

## Conventions to enforce

- **Input variable names** must be CAPITALIZED in all templates, validators, and solutions. Use ALL_CAPS for compound names (e.g. `X_G`, `Y_G`, `N`, `T`).
- **Docstring params**: one per line with a short description (e.g. `X_G: x-coordinate of grass starting position`). Never group params (not `X_G, Y_G: starting position`).
- **Types in C++/Java templates**: use `int` unless the main test set constraints clearly require larger. Templates target newer contestants; they can upgrade types for bonus sets themselves.
- **T** (number of test cases) is always the first line of input and always an uppercase `T`.

## Things to flag during review

- Edge cases not covered by constraints (e.g. two sources at the same position)
- Tie-break behavior when two entities reach a cell simultaneously — must be explicitly defined
- Whether coordinates/values fit in `int` for the main test set
- Any ambiguity in the spread/expansion mechanism (e.g. 4-directional vs 8-directional)
- Return type: ensure the output is a single value per test case unless otherwise justified
