# Create Model Solutions

Write model solutions for a CALICO problem.

## General

Think carefully to thoroughly understand a solution and how it solves the problem before implementing. If a problem statement isn't provided, ask the user for more context.

## Structure

Solutions go in `[problem]/submissions/[accepted|run_time_error|time_limit_exceeded|wrong_answer]/[problem]_[approach].[ext]` (e.g. `mycelium_bfs.py`).

Each solution should mirror the template structure: a `solve(...)` function + `main()` I/O loop. The solve function signature and I/O must match the template exactly.

If the template is discovered to be broken, learn how to create templates and then fix it.

## Conventions

- Input variable names: CAPITALIZED ALL_CAPS, matching the template
- Python: PEP8 — two blank lines between function defs and before `if __name__ == '__main__':`
- Constants (e.g. tick rates, directions) go at module level with descriptive names
- Prioritize clarity and conciseness over micro-optimization — these are educational reference solutions
- Comments should explain the *why* (algorithmic insight), not just the *what*
- Helper functions should go below solve(). This is to help with readability.

## Approach ordering

When problems have multiple test sets, start with the simplest correct solution (e.g. brute force BFS), then build up:
1. **Naive** — easiest to understand and verify correct. Use as ground truth.
2. **Optimized** — introduce one key insight at a time. Each solution should be a diff from the previous unless it's a totally different approach.

When adapting external solutions, rewrite into template style: standard `main()` with `T = int(input())` loop, `solve(...)` function, CAPITALIZED input vars. Don't use `sys.stdin.buffer.read()` bulk parsing unless there's a specific performance reason.

## Verification

When a new solution is added, verify using the check script with a time limit:
```bash
./check -t 4 submissions/accepted/new_sol.py data/sample/00_main.in data/secret/*_main.in
```
If the naive solution is too slow for larger test sets, verify on the small set only, then bootstrap (see threshold-tuning skill).

## Terminology

Follow the terminology closely as written in the problem statement.
