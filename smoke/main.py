#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import override
from calico_lib import (
    Problem,
    Subproblem,
    TestFileBase,
    cpp_runner,
    py_runner,
    run_cli,
)
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os
from os import path

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

class TestCase(NamedTuple):
    N: int
    R: int
    A: list[int]

solution = cpp_runner(
    os.path.join(problem_dir, 'submissions/accepted/smoke_bonus.cpp'),
    os.path.join(problem_dir, 'smoke.bin'))
#solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/smoke_bonus.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))

p = Problem(
    'smoke',
    problem_dir, # problem is in the same directory as the python source file
    test_sets=[
        Subproblem('main', rank=1),
        Subproblem('bonus', rank=2)
    ],
    solution = solution,
    seed = 'smoke19393839382j')

@p.pre_gen_fn
def pre_gen_fn():
    #pass
    solution.compile()

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        lines = [str(len(self.cases))]
        for case in self.cases:
            lines.append(f'{case.N} {case.R}')
            A = ""
            for a in case.A:
                A += str(a) + " "
            lines.append(A)
        return "\n".join(lines) + "\n"

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)
        validator.exec_file(infile)

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(5, 10, [20, 30, 40, 50, 60]),
    TestCase(7, 100, [1, 2, 3, 4, 5, 6, 7]),
    TestCase(8, 5, [5, 10, 17, 30, 36, 45, 50, 56]),
    TestCase(9, 30, [20, 70, 80, 90, 100, 190, 210, 220, 250])
]))

# more ways to add test cases. This is preferred, since running the function is offloaded to run only at test generation.
@p.hidden_test_generator(test_count=4, subproblems=['main', 'bonus'])
def pure_random() -> TestFile:
    test = TestFile([])
    T = random.randint(10, 100)
    for i in range(T):
        R = random.randint(20, 1000)
        N = random.randint(10, 1000)
        a = 0
        A = []
        while len(A) < N:
            a += random.randint(1, int(1e5) // N)
            A.append(a)
        test.cases.append(TestCase(N, R, A))
    return test

@p.hidden_test_generator(test_count=4, subproblems=['bonus'])
def pure_random2() -> TestFile:
    test = TestFile([])
    T = random.randint(10, 100)
    for i in range(T):
        R = random.randint(20, int(1e5))
        N = random.randint(10, int(1e5))
        a = 0
        A = []
        while len(A) < N:
            a += random.randint(1, int(1e9) // N)
            A.append(a)
        test.cases.append(TestCase(N, R, A))
    return test

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    run_cli(p)

    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
