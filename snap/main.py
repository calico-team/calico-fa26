#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

from typing import override
from calico_lib import Problem, cpp_runner, py_runner, TestFileBase, MulticaseTestFile, Subproblem, Runner
from collections.abc import Collection, Iterable
from typing import NamedTuple, override
import random
import os
from os import path

from calico_lib.multicase import TestCaseBase

problem_dir = os.path.dirname(__file__)

p = Problem(
        'snap',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=1),
            ])
class TestCase(NamedTuple):
    M: int
    N: int
    F: int

sol2 = cpp_runner(
        'submissions/accepted/snap.cpp',
        'sol.bin')
validator1 = py_runner('scripts/validator_main.py')
validator2 = py_runner('scripts/validator.py')

@p.pre_gen_fn
def pre_gen_fn():
    random.seed('snapq02394rq2398732894723984')
    sol2.compile()

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        for case in self.cases:
            p.print_test(case.M, case.N, case.F)

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator1.exec_file(infile)
        validator2.exec_file(infile)

    @override
    def write_test_out(self, infile: str):
        p.print_test(sol2.exec_file(infile))

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(4, 7, 2),
    TestCase(1, 23, 2),
    TestCase(9, 8, 10),
    TestCase(1, 1, 1),
    ]))
    
# more ways to add test cases. This is preferred, since running the function is offloaded to run only at test generation.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    test = TestFile([])
    M = 100
    for i in range(10):
        test.cases.append(TestCase(random.randint(1, M), random.randint(1, M), random.randint(1, M)))
    return test

def main():
    # increase stack size for running solutions using heaving recursion
    # import resource
    # resource.setrlimit(resource.RLIMIT_STACK, (268435456, 268435456))

    # TODO: set seed
    p.run_cli()

    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
