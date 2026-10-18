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
    'verity',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=1)
    ],
    solution=None,
    seed='VERITYFALSITYVERITYVERITYCRUELTY')

class TestCase(NamedTuple):
    N: int
    K: int
    A: list[str]

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
        return '\n'.join(lines) + '\n'

    @override
    def write_test_out(self, infile: str = '') -> str:
        """Interactive problems do not write static .out files."""
        return ''

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(4, 4, ['L', 'C', 'F', 'V']),
    TestCase(10, 5, ['A', 'B', 'C', 'D', 'E']),
]))

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])
    T = random.randint(10, 100)
    for _ in range(T):
        N = random.randint(1, 100)
        K = random.randint(1, 26)
        A = random.sample(string.ascii_uppercase, K)

        test.cases.append(TestCase(N, K, A))
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