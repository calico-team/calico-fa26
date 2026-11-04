#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 1e5, N <= 2e5, 0 <= Li <= Ri < 2^(30)

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
    os.path.join(problem_dir, 'submissions/accepted/matcha.cpp'),
    os.path.join(problem_dir, 'matcha.bin'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'matcha',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=4),
    ],
    solution=solution,
    seed='matchaaaaaaa')

class TestCase(NamedTuple):
    N: int 
    L: list[int]
    R: list[int]

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
            lines.append(f'{case.N}')
            lines.append(' '.join(map(str, case.L)))
            lines.append(' '.join(map(str, case.R)))
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(1, [6], [7]),
    TestCase(3, [0, 0, 0], [1073741823, 1073741823, 1073741823]),
    TestCase(4, [0, 1, 3, 5], [1, 2, 4, 8]),
    TestCase(3, [98, 98, 101], [105, 103, 110])
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.

# Anything built from a loop or ``random`` should be a factory, not an
# instance: the factory runs after the library has seeded ``random``.

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=1)
def brute_force() -> TestFile:
    test = TestFile([])
    for one in range(16):
        for two in range(16):
            for three in range(16):
                for four in range(16):
                    L = [one // 4, two // 4, three // 4, four // 4]
                    R = [one % 4, two % 4, three % 4, four % 4]
                    bad = False
                    for i in range(4):
                        if L[i] > R[i]:
                            bad = True
                    if not bad:
                        test.cases.append(TestCase(4, L, R))
    return test


@p.hidden_test_generator(test_count=4)
def pure_random_2() -> TestFile:
    test = TestFile([])
    for _ in range(100):
        N = 2
        L = []
        R = []
        for i in range(N):
            L.append(random.randint(0, (1 << 30) - 1))
            R.append(random.randint(L[-1], (1 << 30) - 1))
        test.cases.append(TestCase(N, L, R))
    return test

@p.hidden_test_generator(test_count=4)
def pure_random_3() -> TestFile:
    test = TestFile([])
    for _ in range(66666):
        N = 3
        L = []
        R = []
        for i in range(N):
            L.append(random.randint(0, (1 << 30) - 1))
            R.append(random.randint(L[-1], (1 << 30) - 1))
        test.cases.append(TestCase(N, L, R))
    return test

@p.hidden_test_generator(test_count=2)
def pure_random_2000() -> TestFile:
    test = TestFile([])
    for _ in range(100):
        N = random.randint(1, 2000)
        L = []
        R = []
        for i in range(N):
            L.append(random.randint(0, (1 << 30) - 1))
            R.append(random.randint(L[-1], (1 << 30) - 1))
        test.cases.append(TestCase(N, L, R))
    return test

@p.hidden_test_generator(test_count=2)
def pure_random_200000() -> TestFile:
    test = TestFile([])
    N = 200000
    L = []
    R = []
    for i in range(N):
        L.append(random.randint(0, (1 << 30) - 1))
        R.append(random.randint(L[-1], (1 << 30) - 1))
    test.cases.append(TestCase(N, L, R))
    return test

def main():
    # Run cli (try `python main.py --help`)
    run_cli(p)

    # Can also specify actions
    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
