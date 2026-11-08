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
#solution = cpp_runner(
#    os.path.join(problem_dir, 'submissions/accepted/rain.cpp'),
#    os.path.join(problem_dir, 'sol.bin'))
solution = py_runner(
    os.path.join(problem_dir, 'submissions/accepted/rain.py')
)
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'rain',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=2),
    ],
    solution=solution,
    seed='bahrain19239120398210')

class TestCase(NamedTuple):
    N: int
    K: int
    L: list[tuple[int, int, int, str]]

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
            lines.append(f'{case.N} {case.K}')
            for X, Y, Z, D in case.L:
                lines.append(f'{X} {Y} {Z} {D}')

        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        # main has tighter constraints (A, B <= 100).
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(3, 3, [ (0, 3, 0, 'E'), (2, 1, 1, 'N'), (8, 8, 2, 'E')]),
    TestCase(4, 2, [ (0, 5, 0, 'E'), (5, 0, 1, 'N'), (1, 3, 2, 'E'), (3, 1, 3, 'N')]),
    TestCase(5, 5, [ (0, 6 , 0, 'E'), (2, 4, 1, 'E'), (4, 2, 2, 'N'), (5, 1, 3, 'N'), (9, 9, 4, 'N')])
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.
p.add_hidden_test(TestFile([
    TestCase(6, 10**9, [
        (1, 10, 5, 'E'),
        (5, 1, 5, 'N'),
        (2, 12, 5, 'E'),
        (8, 2, 5, 'N'),
        (3, 14, 5, 'E'),
        (12, 3, 5, 'N')
    ]),

    TestCase(6, 1, [
        (1, 1, 1, 'E'),
        (2, 1, 1, 'E'),
        (3, 1, 1, 'E'),
        (4, 1, 1, 'E'),
        (5, 1, 1, 'E'),
        (6, 1, 1, 'E')
    ])
]), 'hard_edges')
# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=5)
def random_small() -> TestFile:
    test = TestFile([])

    for _ in range(100):
        N = random.randint(90, 100)
        K = random.randint(1, 10**9)
        L = []
        positions = set()

        for _ in range(N):
            while True:
                X = random.randint(1, 50)
                Y = random.randint(1, 50)
                D = random.choice(['E', 'N'])
                if D == 'N':
                    Z = random.randrange(2, 11, 2)
                else:
                    Z = random.randrange(1, 11, 2)

                if (X, Y) not in positions:
                    positions.add((X, Y))
                    break

            L.append((X, Y, Z, D))

        test.cases.append(TestCase(N, K, L))

    return test


@p.hidden_test_generator(test_count=5)
def random_medium() -> TestFile:
    test = TestFile([])

    for _ in range(10):
        N = random.randint(100, 1000)
        K = random.randint(1, 10**9)
        L = []
        positions = set()

        for _ in range(N):
            while True:
                X = random.randint(1, 100)
                Y = random.randint(1, 100)
                D = random.choice(['E', 'N'])
                if D == 'N':
                    Z = random.randrange(2, 101, 2)
                else:
                    Z = random.randrange(1, 101, 2)

                if (X, Y) not in positions:
                    positions.add((X, Y))
                    break

            L.append((X, Y, Z, D))

        test.cases.append(TestCase(N, K, L))

    return test


@p.hidden_test_generator(test_count=2)
def random_big() -> TestFile:
    test = TestFile([])

    for _ in range(10):
        N = random.randint(1, 10**5)
        K = random.randint(1, 10**9)
        L = []
        positions = set()

        for _ in range(N):
            while True:
                X = random.randint(1, 10**5)
                Y = random.randint(1, 10**5)
                D = random.choice(['E', 'N'])
                if D == 'N':
                    Z = random.randrange(2, 10**5, 2)
                else:
                    Z = random.randrange(1, 10**5, 2)

                if (X, Y) not in positions:
                    positions.add((X, Y))
                    break

            L.append((X, Y, Z, D))

        test.cases.append(TestCase(N, K, L))

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
