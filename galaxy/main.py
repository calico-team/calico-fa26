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
# Built by hand instead of with ``cpp_runner``, which prepends './' to any path
# not starting with '/' and so breaks on Windows absolute paths (C:\...).
solution = cpp_runner(
    os.path.join(problem_dir, 'submissions/accepted/sol_bonus.cpp'),
    os.path.join(problem_dir, 'sol_bonus.bin'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'galaxy',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=2),
        Subproblem('bonus', rank=2)
    ],
    solution=solution,
    seed='mario')

class TestCase(NamedTuple):
    N: int
    M: int 
    Q: int
    G: list[str]
    start: list[tuple[int, int]]
    end: list[tuple[int, int]]

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
            lines.append(f'{case.N} {case.M} {case.Q}')
            lines += case.G
            for i in range(case.Q):
                lines.append(f'{case.start[i][0]} {case.start[i][1]} {case.end[i][0]} {case.end[i][1]}')
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        # main has tighter constraints (A, B <= 100).
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)
        validator.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(2,4,2,[".R.B", ".RRB"],[(0,0),(1,0)],[(1,3),(1,3)]),
    TestCase(2,4,2,[".RB.", ".RB."],[(0,0),(0,3)],[(1,3),(1,3)]),
    TestCase(9,9,3,["BR.R.R.R.", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "B.B.B.B.B"],[(8,1),(0,4),(8,7)],[(8,8),(8,8),(8,8)])
]))

p.add_sample_test(TestFile([
    TestCase(2,4,2,[".RB.", ".RB."],[(1,0),(1,3)],[(1,2),(0,3)]),
    TestCase(9,9,3,["BR.R.R.R.", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "B.B.B.B.B"],[(0,8),(8,1),(8,7)],[(4,5),(2,8),(0,0)])
]), subproblems=["bonus"])

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.
# p.add_hidden_test(TestFile([
#     TestCase(1, 1),
#     TestCase(100, 100),
#     TestCase(1, 100),
# ]), 'edges')

# # Anything built from a loop or ``random`` should be a factory, not an
# # instance: the factory runs after the library has seeded ``random``.
# def iota() -> TestFile:
#     """Generate 80 cases: X counts up 1..80, Y counts down 80..1."""
#     return TestFile([TestCase(i + 1, 80 - i) for i in range(80)])

# p.add_hidden_test(iota, 'iota')

# def iota_bonus() -> TestFile:
#     """Generate 100 bonus-sized cases: X up 1..100, Y down 10000..9901."""
#     return TestFile([TestCase(i + 1, 10000 - i) for i in range(100)])

# p.add_hidden_test(iota_bonus, 'iota', subproblems=['bonus'])

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random_main() -> TestFile:
    """Generate a test file with 100 random cases, valid for every subproblem."""
    test = TestFile([])
    for _ in range(100):
        N, M, Q = random.randint(1, 200), random.randint(1, 200), random.randint(1, 1000)
        G = []
        normal_tiles = []
        for i in range(N):
            row = ""
            for j in range(M):
                cell = random.choice(['R', 'B', '.'])
                row += cell
                if cell == '.':
                    normal_tiles.append((i, j))
            G.append(row)
        if len(normal_tiles) == 0:
            row, col = random.randint(0, N-1), random.randint(0, M-1)
            G[row][col] = '.'
            normal_tiles.append((row, col))
        
        start = []
        end = [(N-1, M-1) for _ in range(Q)]
        for i in range(Q):
            start.append(random.choice(normal_tiles))

        test.cases.append(TestCase(N, M, Q, G, start, end))
    return test

@p.hidden_test_generator(test_count=4, subproblems=["bonus"])
def pure_random_bonus() -> TestFile:
    """Generate a test file with 100 random cases, valid for every subproblem."""
    test = TestFile([])
    for _ in range(100):
        N, M, Q = random.randint(1, 200), random.randint(1, 200), random.randint(1, 1000)
        G = []
        normal_tiles = []
        for i in range(N):
            row = ""
            for j in range(M):
                cell = random.choice(['R', 'B', '.'])
                row += cell
                if cell == '.':
                    normal_tiles.append((i, j))
            G.append(row)
        if len(normal_tiles) == 0:
            row, col = random.randint(0, N-1), random.randint(0, M-1)
            G[row][col] = '.'
            normal_tiles.append((row, col))
        
        start = []
        end = []
        for i in range(Q):
            start.append(random.choice(normal_tiles))
            end.append((random.randint(0, N-1), random.randint(0, M-1)))

        test.cases.append(TestCase(N, M, Q, G, start, end))
    return test

# @p.hidden_test_generator(test_count=4, subproblems=['bonus'])
# def pure_random2() -> TestFile:
#     """Generate a test file with 100 random bonus-sized cases."""
#     cases = (TestCase(random.randint(70, int(1e12)), random.randint(70, int(1e12))) for _ in range(100))
#     return TestFile(cases)

def main():
    # Run cli (try `python main.py --help`)
    run_cli(p)

    # Can also specify actions
    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
