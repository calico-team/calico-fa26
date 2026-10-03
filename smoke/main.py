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
        'smoke',
        problem_dir, # problem is in the same directory as the python source file
        test_sets=[
            Subproblem('main', rank=1),
            ])
class TestCase(NamedTuple):
    R: int
    N: int
    T: list[int]

sol2 = cpp_runner(
        'submissions/accepted/smoke.cpp',
        'sol.bin')

sol = py_runner(
        'submissions/accepted/smoke.py',
)
validator1 = py_runner('scripts/validator_main.py')
validator2 = py_runner('scripts/validator.py')

@p.pre_gen_fn
def pre_gen_fn():
    random.seed('smoke19393839382j')
    sol2.compile()

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self):
        """Write the input file of this test case using print_test"""
        p.print_test(len(self.cases))
        lines = [str[len(self.cases)]]
        for case in self.cases:
            lines.append(f'{case.R} {case.N}')
            T = ""
            for t in case.T:
                T += str(t) + " "
            lines.append(T)
        return "\n".join(lines) + "\n"

    @override
    def validate_test_in(self, infile: str):
        """Verify the test using an external validator."""
        if 'main' in self.subproblems:
            validator1.exec_file(infile)
        validator2.exec_file(infile)

# adds to all subproblems by default
p.add_sample_test(TestFile([
    TestCase(1, 3, [20, 30, 60]),
    TestCase(1, 3, [20, 30, 50]),
    TestCase(1, 4, [1, 2, 41, 42]),
]))

# more ways to add test cases. This is preferred, since running the function is offloaded to run only at test generation.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    test = TestFile([])
    for i in range(10):
        R = random.randint(20, 200)
        N = random.randint(1, 100)
        t = 0
        T = []
        while len(T) < N:
            t += random.randint(1, 100)
            T.append(t)
        test.cases.append(TestCase(R, N, T))
    return test

# @p.hidden_test_generator(test_count=4)
# def pure_random2():
#     cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
#     return TestFile(cases)

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
