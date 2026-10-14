# Design Constraints

Iteratively adjust constraint thresholds so that each solution passes exactly the test sets it's intended for.

## Goal

For each solution and test set, achieve one of:
- **Pass**: correct output, well within time limit (with wiggle room for student implementations)
- **TLE**: exceeds time limit, confirming the test set requires a faster approach

A solution should pass all test files in its intended sets and TLE on at least one file in the next harder set.

## Bootstrapping correctness

Build up from slow-but-provably-correct to fast:

1. Start with a brute-force solution that is obviously correct (e.g., naive BFS).
2. Generate easy tests (main set) using the brute force as the runner in main.py.
3. Write a faster solution. Verify it produces identical output on the easy tests.
4. Use the faster solution as the runner. Generate harder tests (next set).
5. Repeat: each new solution is verified against the previous tier's tests before being trusted to generate the next tier.

This chain of trust ensures correctness without needing a proof for every optimization.

## Tuning workflow

1. **Generate tests**: `timeout 120 python main.py` (use the fastest available solution as runner)
2. **Test each solution** on its intended sets:
   ```bash
   ./check -t 4 submissions/accepted/slow_sol.py data/secret/*_main.in
   ./check -t 4 submissions/accepted/fast_sol.py data/secret/*_main.in data/secret/*_bonus1.in
   ```
3. **Verify TLE separation**: run the slower solution on the harder set, confirm it TLEs:
   ```bash
   ./check -t 4 submissions/accepted/slow_sol.py data/secret/*_bonus1.in
   ```
4. **Evaluate the results**:
   - If intended solutions pass with lots of room (e.g., 200ms on a 4s limit), thresholds might be too easy — consider increasing MAX_COORD.
   - If intended solutions barely pass or TLE, thresholds are too hard — decrease MAX_COORD.
   - If the slower solution passes all harder tests, thresholds are too easy for separation — increase MAX_COORD for that set.
   - Give more leeway to easier ranks (rank 2 main) and less to harder ranks (rank 4). Students solving rank 4 should have tight, efficient implementations.
5. **Adjust and repeat**: update `constants.py`, regenerate tests, and re-check. This is a back-and-forth — the user provides problem-specific intuition on what thresholds make sense.

## Batch testing with run_all_tests.sh

Use `run_all_tests.sh` to test multiple solutions against multiple sets in one invocation. Comment/uncomment lines to focus on the boundary you're tuning. Always split `python main.py` (regenerate) and `bash run_all_tests.sh` (check) into separate commands for responsiveness.

## Key principles

- **Single source of truth**: constraint constants live in `constants.py`. Both `main.py` and validators import from it.
- **Always use timers**: `timeout` for generation, `-t` for checking. Never let a process run unbounded.
- **Wiggle room**: intended solutions should pass with ~2-3x margin on time. Rank 1-2 tests should be very generous; rank 3-4 can be tighter.
- **Separation**: the slower solution must reliably TLE on the harder set — ideally TLE on ALL files, not just the stress test. If random tests are too easy, use `random_outer_case` to force large separations.
- **Be honest about gaps**: if two solutions have the same asymptotic complexity and you can't get clean separation no matter how you tune T and MAX_COORD, tell the user. This means the optimization isn't a big enough jump to warrant its own test set. A clean boundary comes from a real complexity class difference.
