#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

import os
import random
from collections.abc import Iterable
from typing import NamedTuple, override

from calico_lib import (
    Problem,
    Subproblem,
    TestFileBase,
    cpp_runner,
    py_runner,
    run_cli,
)

# All generated files live under this directory.
problem_dir = os.path.dirname(__file__)

# Reference solution (auto-generates answers) and input validators.
# Paths are absolute so generation works from any working directory.
solution = cpp_runner(
    os.path.join(problem_dir, 'submissions/accepted/sol.cpp'),
    os.path.join(problem_dir, 'sol.bin'))
# solution = py_runner(os.path.join(problem_dir, "submissions/accepted/sol.py"))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
# validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'schedule',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=2),
    ],
    solution=solution,
    seed='add_seed_600')

class TestCase(NamedTuple):
    N: int
    M: int
    K: int
    P: list[int]

@p.pre_gen_fn
def pre_gen_fn():
    """Compile the cpp solution once before generation (the library won't)."""
    solution.compile()

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self) -> str:
        """Return the full input: the case count, then one ``X Y`` per case."""
        lines = [str(len(self.cases))]
        for case in self.cases:
            lines.append(f'{case.N} {case.M} {case.K}')
            lines.append(" ".join(map(str, case.P)))
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        # main has tighter constraints (A, B <= 100).
        # if 'main' in self.subproblems:
            # validator_main.exec_file(infile)
        validator.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(8, 3, 8, [0, 1, 2, 3, 4, 5, 6, 7]),
    TestCase(8, 1, 8, [0, 0, 0, 0, 0, 0, 0, 0]),
    TestCase(8, 4, 2, [0, 7, 2, 3, 2, 2, 1, 2]),
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.
p.add_hidden_test(TestFile([
    TestCase(6, 2, 3, [3, 4, 0, 0, 0, 0]),
    TestCase(6, 2, 3, [0, 0, 0, 0, 1, 2]),
    TestCase(12, 6, 2, [0, 1, 2, 3, 4, 5, 0, 7, 7, 0, 10, 10]),
    TestCase(4, 2, 2, [0, 4, 0, 0]),
    TestCase(6, 3, 2, [0, 0, 2, 3, 0, 0])
]), 'edges')

# Random tests are factories too, for the same seeding reason.
# Big random
@p.hidden_test_generator(test_count=2)
def pure_random() -> TestFile:
    """Generate a test file purely randomly"""
    test = TestFile([])
    for _ in range(10):
        N = random.randint(1000, 10000)
        M = random.randint(1, 50000)
        K = random.randint(1, N)
        P = [random.randint(0, N) for _ in range(N)]
        for i in range(1, N+1):
            seen = set([i])
            while i != 0:
                if P[i-1] in seen:
                    P[i-1] = 0
                i = P[i-1]
                seen.add(i)
        test.cases.append(TestCase(N, M, K, P))
    return test

# Tree heights (nodes on the longest root-to-leaf path) are capped so the
# recursive DFS in sol.py stays under Python's default recursion limit (1000,
# minus a few frames for main/solve).
MAX_DEPTH = 900

def taller_case(chainy: bool) -> TestCase:
    """One tall, bushy forest with N near the max so a PQ is required.

    M is kept below the tallest tree so not every task gets done and the
    greedy order matters; K is small relative to the ready set so many tasks
    compete each day. ``chainy`` uses window 1 -> long chains (each up to D).
    """
    N = random.randint(8000, 10000)
    D = random.randint(MAX_DEPTH // 2, MAX_DEPTH)  # depth cap for this case
    window = 1 if chainy else random.randint(2, 8)
    root_prob = random.choice([0.0, 0.001, 0.01, 0.05])
    order = list(range(1, N+1)); random.shuffle(order)
    P = [0] * N
    depth = [0] * (N + 1)  # depth[v] = nodes on path from root to v
    for idx, v in enumerate(order):
        par = 0
        if idx > 0 and random.random() >= root_prob:
            cand = order[random.randint(max(0, idx - window), idx - 1)]
            if depth[cand] < D:
                par = cand
        P[v-1] = par
        depth[v] = depth[par] + 1 if par else 1
    height = max(depth)
    M = random.randint(max(1, height // 4), height)
    K = random.randint(1, max(1, 2 * N // height))
    return TestCase(N, M, K, P)

@p.hidden_test_generator(test_count=4)
def taller_random() -> TestFile:
    """10 tall cases per file."""
    return TestFile(taller_case(t == 0) for t in range(10))

@p.hidden_test_generator(test_count=2)
def taller_random_max_t() -> TestFile:
    """T = 100 (validator max) tall cases per file, so slow solutions TLE."""
    return TestFile(taller_case(t % 10 == 0) for t in range(100))

def main():
    # Run cli (try `python main.py --help`)
    run_cli(p)

    # Can also specify actions
    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
