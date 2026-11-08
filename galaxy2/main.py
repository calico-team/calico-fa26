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
    os.path.join(problem_dir, 'submissions/accepted/sol.cpp'),
    os.path.join(problem_dir, 'sol.bin'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'galaxy2',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=3, time_limit=4),
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
    K: list[int]

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
                lines.append(f'{case.start[i][0]} {case.start[i][1]} {case.end[i][0]} {case.end[i][1]} {case.K[i]}')
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
    TestCase(2,4,2,[".R.B", ".RRB"],[(0,0),(1,0)],[(1,3),(1,3)],[6,6]),
    TestCase(2,4,2,[".RB.", ".RB."],[(1,0),(1,3)],[(1,2),(0,3)],[10,1]),
    TestCase(9,9,3,["BR.R.R.R.", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "BRBRBRBRB", "B.B.B.B.B"],[(0,8),(8,1),(8,7)],[(4,5),(2,8),(0,1)],[8,12,20])
]))

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

p.add_hidden_test(TestFile([
    TestCase(1,1,1,["."],[(0,0)],[(0,0)],[0]),
    TestCase(1,5,2,[".RB.."],[(0,0),(0,3)],[(0,4),(0,4)],[1000000000,1]),
    TestCase(4,1,1,[".","R","R","B"],[(0,0)],[(3,0)],[3]),
    TestCase(4,1,1,[".","B","B","B"],[(0,0)],[(3,0)],[1000000000]),
    TestCase(2,2,1,[".B","BR"],[(0,0)],[(1,1)],[1000000000]),
    TestCase(2,2,1,["..",".R"],[(0,0)],[(1,1)],[2]),
    TestCase(1,4,1,[".R.B"],[(0,0)],[(0,3)],[5]),
    TestCase(3,3,3,["BRB","R.R","BRB"],[(1,1),(1,1),(1,1)],[(1,1),(0,1),(0,0)],[0,2,1000000000]),
    TestCase(1,5,2,[".BBB."],[(0,0),(0,4)],[(0,4),(0,0)],[3,4]),
    TestCase(1,5,3,[".BRB."],[(0,0),(0,0),(0,4)],[(0,4),(0,1),(0,2)],[1000000000,1,1]),
    TestCase(1,5,2,[".RRRB"],[(0,0),(0,0)],[(0,3),(0,4)],[3,1000000000]),
    TestCase(3,3,2,["RRR","RBR","RR."],[(2,2),(2,2)],[(1,1),(0,0)],[4,5])
]), 'edges')

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=2)
def pure_random() -> TestFile:
    test = TestFile([])
    total = 4 * 10**4
    while len(test.cases) < 100 and total > 0:
        N = random.randint(1, min(10, total))
        M = random.randint(1, min(4000, total // N))
        Q = random.randint(1, 1000)
        total -= N * M
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
            G[row] = G[row][:col] + '.' + G[row][col+1:]
            normal_tiles.append((row, col))

        start = []
        end = []
        K = []
        for i in range(Q):
            s = random.choice(normal_tiles)
            e = (random.randint(0, N-1), random.randint(0, M-1))
            start.append(s)
            end.append(e)
            K.append(abs(s[0] - e[0]) + abs(s[1] - e[1]) + random.randint(0, 6))

        test.cases.append(TestCase(N, M, Q, G, start, end, K))
    return test

def snake(N: int, M: int, pattern: str) -> tuple[list[str], list[tuple[int, int]]]:
    grid = [['R' if (i + j) % 2 else 'B' for j in range(M)] for i in range(N)]
    path = []
    for k in range(0, N, 3):
        cols = range(M) if k // 3 % 2 == 0 else range(M-1, -1, -1)
        for j in cols:
            path.append((k, j))
        if k + 3 < N:
            j = M-1 if k // 3 % 2 == 0 else 0
            path.append((k+1, j))
            path.append((k+2, j))
    for i, (row, col) in enumerate(path):
        grid[row][col] = pattern[i % len(pattern)]
    return [''.join(row) for row in grid], path

def chain_cases(flip: bool) -> TestFile:
    N, M, Q = 10, 4000, 10**5
    if flip:
        G, path = snake(M, N, '.RR.BB')
    else:
        G, path = snake(N, M, '.RR.BB')

    start = []
    end = []
    K = []
    for i in range(Q):
        s = random.randrange(0, len(path), 3)
        e = random.randrange(len(path))
        start.append(path[s])
        end.append(path[e])
        K.append(max(0, abs(e - s) * 4 // 3 + random.randint(-2, 2)))

    if flip:
        G = [''.join(G[i][j] for i in range(M)) for j in range(N)]
        start = [(col, row) for row, col in start]
        end = [(col, row) for row, col in end]

    return TestFile([TestCase(N, M, Q, G, start, end, K)])

@p.hidden_test_generator(test_count=1)
def regions() -> TestFile:
    N, M, Q = 10, 4000, 10**5
    G, path = snake(N, M, '.R.B')
    half = len(path) // 2
    start = []
    end = []
    K = []
    for i in range(Q):
        start.append(path[random.randrange(0, half, 2)])
        end.append(path[random.randrange(half, len(path))])
        K.append(10**9)
    return TestFile([TestCase(N, M, Q, G, start, end, K)])

@p.hidden_test_generator(test_count=1)
def chain() -> TestFile:
    return chain_cases(False)

@p.hidden_test_generator(test_count=1)
def chain_flipped() -> TestFile:
    return chain_cases(True)

@p.hidden_test_generator(test_count=1)
def normal_grid() -> TestFile:
    N, M, Q = 10, 4000, 10**5
    G = ['.' * M for _ in range(N)]
    start = []
    end = []
    K = []
    for i in range(Q):
        s = (random.randint(0, N-1), random.randint(0, M-1))
        e = (random.randint(0, N-1), random.randint(0, M-1))
        start.append(s)
        end.append(e)
        K.append(abs(s[0] - e[0]) + abs(s[1] - e[1]) + random.randint(0, 2))
    return TestFile([TestCase(N, M, Q, G, start, end, K)])

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
