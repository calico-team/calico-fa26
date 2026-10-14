#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

import os
import random
import string
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

# Input validators.
# Paths are absolute so generation works from any working directory.
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``seed`` is handled by the library: it calls ``random.seed`` before each test,
# so you can't forget to seed. For interactive problems, set solution=None.
p = Problem(
    'add_test_fa26',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=1, time_limit= 2, mem_limit= 1_000_000_000), #is the mem limit always a million?
        Subproblem('bonus', rank=2, time_limit=4, mem_limit=1_000_000_000),
    ],
    solution=None,
    seed='add_seed_600')

class TestCase(NamedTuple):
    N: int
    K: int
    A: list[str]
    solution: list[str]

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self) -> str:
        """Return the full input: case count, then N, K, A, and secret solution per case."""
        lines = [str(len(self.cases))]
        for case in self.cases:
            lines.append(f'{case.N} {case.K}')
            lines.append(' '.join(case.A))
            lines.append(''.join(case.solution).replace(' ', ''))
        return '\n'.join(lines) + '\n'

    @override
    def write_test_out(self, infile: str = '') -> str:
        """Interactive problems do not write static .out files."""
        return ''

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        # main has tighter constraints (A, B <= 100).
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)
        validator.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(4, 2, ['A', 'B'], ['A', 'B', 'A', 'B']),
    TestCase(1, 1, ['X'], ['X']),
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.
p.add_hidden_test(TestFile([
    TestCase(1, 1, ['A'], ['A']),
    TestCase(2, 2, ['A', 'B'], ['B', 'A']),
]), 'edges')

# Anything built from a loop or ``random`` should be a factory, not an
# instance: the factory runs after the library has seeded ``random``.
def iota() -> TestFile:
    """Generate cases with increasing N and structured input."""
    cases = []
    for i in range(80):
        n = i + 1
        k = min(26, max(1, 80 - i))
        type_of_ity = list(string.ascii_uppercase[:k])
        answer = [random.choice(type_of_ity) for _ in range(n)]
        cases.append(TestCase(n, k, type_of_ity, answer))
    return TestFile(cases)

p.add_hidden_test(iota, 'iota')

def iota_bonus() -> TestFile:
    """Generate 100 bonus-sized cases."""
    cases = []
    for i in range(100):
        n = (i + 1) * 10
        k = 26
        type_of_ity = list(string.ascii_uppercase)
        answer = [random.choice(type_of_ity) for _ in range(n)]
        cases.append(TestCase(n, k, type_of_ity, answer))
    return TestFile(cases)

p.add_hidden_test(iota_bonus, 'iota', subproblems=['bonus'])

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])
    for _ in range(10):
        n = random.randint(1, 100)
        k = random.randint(1, 26)
        typeOfIty = random.sample(string.ascii_uppercase, k)
        answer = []
        for _ in range(n):
            answer.append(random.choice(typeOfIty))

        test.cases.append(TestCase(n, k, typeOfIty, answer))
    return test

@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
def pure_random2() -> TestFile:
    """Generate a test file with 100 random bonus-sized cases."""
    test = TestFile([])
    for _ in range(100):
        n = random.randint(100, 1000)
        k = random.randint(1, 26)
        typeOfIty = random.sample(string.ascii_uppercase, k)
        answer = [random.choice(typeOfIty) for _ in range(n)]
        test.cases.append(TestCase(n, k, typeOfIty, answer))
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