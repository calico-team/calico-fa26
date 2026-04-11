# Design Tests

Generate tests and verify solutions for a CALICO problem.

## Validators

One validator script per test set in `[problem]/scripts/`:
- `validator.py` — global (loosest constraints, applies to all sets)
- `validator_main.py` — main set constraints
- `validator_[setname].py` — one per additional test set (bonus1, bonus2, etc.)

Each validator reads stdin, asserts all constraints, exits 0 on success. Use the template I/O pattern (read T, loop, parse each case). Always assert distinctness constraints.

Validators import thresholds from `constants.py` (in the problem root) using:
```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from constants import BONUS1_MAX_T, BONUS1_MAX_COORD
```

## constants.py

Lives in the problem root directory. Single source of truth for all constraint thresholds (`MAIN_MAX_T`, `MAIN_MAX_COORD`, `BONUS1_MAX_T`, etc.). Imported by both `main.py` and all validators.

## main.py

The test generation script. Key pieces:
- Imports thresholds from `constants.py` — do NOT duplicate constants at the top of main.py
- `Problem(...)` with `Subproblem` entries per test set
- `TestCase` as a `NamedTuple` with CAPITALIZED field names
- `TestFile(TestFileBase)` with `write_test_in`, `validate_test_in`, `write_test_out`
- `py_runner(...)` for the model solution (used to generate `.ans` files) — always use the most efficient available solution as the runner
- `validate_test_in` should dispatch to the tightest applicable validator based on subproblems
- Sample test via `p.add_sample_test(...)` — tag with all subproblems so it's included in every zip
- Edge cases via `p.add_hidden_test(..., 'name', subproblems=[...])`
- Random tests via `@p.hidden_test_generator(test_count=N, subproblems=[...])`
- Easier test sets should be tagged with all harder subproblems too (e.g., main tests get `['main', 'bonus1', 'bonus2', 'bonus3']`) so they appear in all zips

Use a `random_case(lo, hi)` helper that generates valid cases within bounds.

For harder test sets, use `random_outer_case(lo, hi)` to force large separation — e.g., 50% chance X coords are far apart, 50% chance Y coords are far apart. This prevents random cases from being too easy relative to stress tests.

Comment out test sets that don't have a fast enough solution to generate answers yet.

## Test case design

- **Edge cases**: minimum distance (adjacent), max corners, axis-aligned, diagonal, same row/column
- **Random**: use the MAX_T and MAX_COORD constants from constants.py
- **Outer random**: force coordinates to the outer 10% of range for harder random tests
- **Axis-aligned**: near-maximal separation on one axis, close (+/-5) on the other, with the close pair shifted to a random position along the free axis. Tests nearly-axis-aligned configurations that can behave differently from diagonal cases.
- **Stress**: worst-case inputs (max distance corners, repeated worst case)

## run_all_tests.sh

Batch test script in the problem root. Tests multiple solutions against multiple test sets in one run.

Key structure:
- `SOLS` array: list all solutions (Python, then Java, then C++)
- `SETS` array: `"setname:glob_pattern"` entries — comment/uncomment to scope the run
- Language-specific time limits: `TL_PY=4`, `TL_JAVA=2`, `TL_CPP=1`
- Always use `-f` (fail-fast) flag in check invocations
- Use `PY_CMD=python3` prefix for Python, `CPP_CC="g++ -std=c++17"` for C++

Example invocation per language:
```bash
PY_CMD=python3 ./check -t $TL_PY -f "$sol" $files 2>&1
./check -t $TL_JAVA -f "$sol" $files 2>&1
CPP_CC="g++ -std=c++17" ./check -t $TL_CPP -f "$sol" $files 2>&1
```

## Threshold tuning

**Hard constraint**: time limits across languages are fixed ratios imposed by the judge platform — `py = 4×cpp`, `java = 2×cpp`. You cannot adjust them independently. The only lever is `constants.py`.

Tuning process (one test set at a time):
1. Run `run_all_tests.sh` with the target set active
2. Identify the slowest solution that *should* pass — if it TLEs, lower `MAX_COORD` in `constants.py`
3. Identify the fastest solution that *should* TLE — if it passes, lower `MAX_COORD` further
4. After changing a threshold, run `python3 main.py` to regenerate tests, then re-run
5. Repeat until all expected pass/TLE behaviors hold for all three languages

When evaluating a threshold candidate, test all three languages — a threshold that works for C++ may still TLE the Java or Python equivalent.

## Generating tests

Run `python3 main.py` from the problem directory. Always use a timeout to prevent runaway generation:
```
timeout 120 python3 main.py
```

The timeout should be roughly `(4s per test file) * 2x overhead`. If generation is too slow, you need a faster solution or smaller thresholds.

## Check script

Use the `./check` script to verify solutions against generated test files:
```bash
# Run specific tests with a time limit
PY_CMD=python3 ./check -t 4 submissions/accepted/sol.py data/secret/*_main.in

# Java (compiled by check script automatically)
./check -t 2 submissions/accepted/sol.java data/secret/*_bonus1.in

# C++ with C++17
CPP_CC="g++ -std=c++17" ./check -t 1 submissions/accepted/sol.cpp data/secret/*_bonus2.in

# Stop on first error (WA or TLE)
./check -t 4 -f submissions/accepted/sol.py data/secret/*_bonus2.in
```

The `-t` flag sets a per-test-file time limit in seconds. **Always use a time limit** to prevent hanging. The check script reports timing for each test and detects TLE (exit code 124 or elapsed > limit).

The `-f` / `--fail-fast` flag stops execution on the first error (WA or TLE). Use it by default.

Time limit guidelines:
- Python: 4s (`PY_CMD=python3`)
- Java: 2s
- C++: 1s (`CPP_CC="g++ -std=c++17"`)

## Wrong answer solutions

Place intentionally incorrect solutions in `[problem]/submissions/wrong_answer/`. These verify that the test suite catches common mistakes. Include them in `run_all_tests.sh` — they should WA on at least some test set.
