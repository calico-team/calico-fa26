# Create Model Solutions

Creating model solutions for ANY CALICO problem.

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

### C++ conventions

- C++ / Java: when it makes sense to depending on the constraints of the main test set and problem statement, prefer `int` for main test set constraints (not `long long`/`long`). If the main test set requires long though you should use long.
    - C++: use `typedef long long ll`.
- Use `using namespace std;`
- Watch for integer overflow. Use `ll` for any computation derived from large inputs.

### Java conventions

- For novice-facing (rank2 / main set) solutions, clarity trumps performance

## Target audience by rank

Solutions are written for specific target audiences. Calibrate complexity accordingly:

- **Rank 1**: High school student with very beginner CS knowledge. Solutions must be super readable with a focus on being educational.
- **Rank 2**: High school student with general CS knowledge. Lean toward explicit readability — avoid fancy language features, prefer simple data structures, verbose variable names, step-by-step logic.
- **Rank 3**: High school student with strong CS background and some competitive programming experience. Advanced features (custom hashes, binary search, pruning) and algorithms are appropriate.
- **Rank 4**: Olympiad-level. No need to hold back — advanced math, obscure algorithms, research-paper techniques, etc.

## Approach ordering

When problems have multiple test sets, start with the simplest correct solution (e.g. brute force BFS), then build up:
1. **Naive** — easiest to understand and verify correct. Use as ground truth.
2. **Optimized** — introduce one key insight at a time. Each solution should be a diff from the previous unless it's a totally different approach.

When adapting external solutions, rewrite into template style: standard `main()` with `T = int(input())` loop, `solve(...)` function, CAPITALIZED input vars. Don't use `sys.stdin.buffer.read()` bulk parsing unless there's a specific performance reason.

## Verification

Use the check script. As of writing most check scripts for problems are not up-to-date with the latest feaatuers: time limits (-t), fail-fast (-f), Java compilation (javac -d java_bin), TLE detection, timing output, etc. Check /example to copy the updated script.

When a new solution is added, verify using the check script with a time limit:
```bash
./check -t 4 submissions/accepted/new_sol.py data/sample/00_main.in data/secret/*_main.in
```
For Java: `./check -t 2 submissions/accepted/new_sol.java ...`
For C++: `CPP_CC="g++ -std=c++17" ./check -t 1 submissions/accepted/new_sol.cpp ...`

If the naive solution is too slow for larger test sets, verify on the small set only, then bootstrap (see threshold-tuning skill).

TODO add info about run_all_tests.sh here

## Multi-language porting

When porting Python solutions to Java and C++:

1. Port all solutions before running batch tests — easier to fix patterns across the board.
2. Verify each language compiles and gives correct output on sample tests before moving on.
3. Then run `run_all_tests.sh` across all sets and tune thresholds (see design-tests skill).

## Terminology

Follow the terminology closely as written in the problem statement.
