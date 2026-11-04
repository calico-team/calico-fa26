#!/usr/bin/env python3

# Dictionary: 
# Constraints:
#   main: T <= 100, N <= 2e5, 1 <= Ai <= N, 0 <= Vi < 2^(30)

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
    os.path.join(problem_dir, 'submissions/accepted/dictionary.cpp'),
    os.path.join(problem_dir, 'dictionary.bin'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'dictionary',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=4, time_limit=2),
    ],
    solution=solution,
    seed='dictionaryyyyy')

class TestCase(NamedTuple):
    N: int
    A: list[int]
    V: list[int]

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
            lines.append(' '.join(map(str, case.A)))
            lines.append(' '.join(map(str, case.V)))
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(2, [1, 2], [1, 2]),
    TestCase(2, [2, 1], [3, 7]),
    TestCase(2, [1, 1], [3, 7])
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.

# Anything built from a loop or ``random`` should be a factory, not an
# instance: the factory runs after the library has seeded ``random``.

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random_small() -> TestFile:
    test = TestFile([])
    for _ in range(100):
        N = random.randint(1, 2000)
        A = []
        V = []
        for i in range(N):
            A.append(random.randint(1, N))
            V.append(random.randint(0, (1 << 30) - 1))
        test.cases.append(TestCase(N, A, V))
    return test

@p.hidden_test_generator(test_count=4)
def pure_random_big() -> TestFile:
    test = TestFile([])
    N = 200000
    A = []
    V = []
    for i in range(N):
        A.append(random.randint(1, N))
        V.append(random.randint(0, (1 << 30) - 1))
    test.cases.append(TestCase(N, A, V))
    return test

@p.hidden_test_generator(test_count=4)
def big_cycle() -> TestFile:
    test = TestFile([])
    N = 200000
    A = [i for i in range(1, N + 1)]
    random.shuffle(A)
    V = []
    for i in range(N):
        V.append(random.randint(0, (1 << 30) - 1))
    test.cases.append(TestCase(N, A, V))
    return test

@p.hidden_test_generator(test_count=4)
def long_tree() -> TestFile:
    test = TestFile([])
    N = 200000
    seq = [i for i in range(1, N + 1)]
    random.shuffle(seq)
    A = [0] * N 
    A[seq[0] - 1] = seq[0]
    V = []
    for i in range(1, N):
        A[seq[i] - 1] = seq[i - 1]
    for i in range(N):
        V.append(random.randint(0, (1 << 30) - 1))
    test.cases.append(TestCase(N, A, V))
    return test

@p.hidden_test_generator(test_count=4)
def half_cycle_half_tree() -> TestFile:
    test = TestFile([])
    N = 200000
    cyc = random.sample(range(1, N + 1), 100000)
    oth = list(set(range(1, N + 1)) - set(cyc))
    random.shuffle(oth)
    A = [0] * N
    V = []
    for i in range(len(cyc)):
        A[cyc[i] - 1] = cyc[(i + 1) % len(cyc)]
    A[oth[0] - 1] = cyc[0]
    for i in range(1, len(oth)):
        A[oth[i] - 1] = oth[i - 1]
    for i in range(N):
        V.append(random.randint(0, (1 << 30) - 1))
    test.cases.append(TestCase(N, A, V));
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
