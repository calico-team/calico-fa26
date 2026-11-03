#!/usr/bin/env python3

import os
import random
from collections.abc import Iterable
from typing import NamedTuple, override

from calico_lib import Problem, Subproblem, TestFileBase, cpp_runner, py_runner, run_cli

problem_dir = os.path.dirname(__file__)
solution = cpp_runner(
    os.path.join(problem_dir, 'submissions/accepted/sol.cpp'),
    os.path.join(problem_dir, 'sol.bin'),
)
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

MAX_T = 10_000
MAX_CELLS = 100_000
MAX_Q = 10_000

p = Problem(
    'paintball',
    problem_dir,
    test_sets=[Subproblem('main', rank=3)],
    solution=solution,
    seed='paintball_seed_678128904567890',
)


class Paintball(NamedTuple):
    x: int
    y: int
    color: str
    radius: int


class TestCase(NamedTuple):
    rows: int
    cols: int
    paintballs: tuple[Paintball, ...]


@p.pre_gen_fn
def pre_gen_fn():
    solution.compile()

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self) -> str:
        lines = [str(len(self.cases))]
        for case in self.cases:
            lines.append(f'{case.rows} {case.cols} {len(case.paintballs)}')
            lines.extend(
                f'{ball.x} {ball.y} {ball.color} {ball.radius}'
                for ball in case.paintballs
            )
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)
        validator.exec_file(infile)


def shot(x: int, y: int, color: str, radius: int) -> Paintball:
    return Paintball(x, y, color, radius)


def random_case(rows: int, cols: int, q: int) -> TestCase:
    """Make a valid case with circles of varied sizes and positions."""
    balls = []
    for i in range(q):
        x = random.randint(1, cols)
        y = random.randint(1, rows)
        max_radius = min(x - 1, cols - x, y - 1, rows - y)
        radius = random.randint(0, max_radius)
        balls.append(shot(x, y, chr(ord('A') + i % 26), radius))
    return TestCase(rows, cols, tuple(balls))


# statement samples
p.add_sample_test(TestFile([
    TestCase(7, 7, (shot(4, 4, 'X', 3),)),
    TestCase(3, 5, (shot(3, 2, 'W', 1), shot(4, 2, 'I', 1), shot(4, 2, 'G', 0))),
    TestCase(3, 1, (shot(1, 2, 'A', 0), shot(1, 2, 'B', 0), shot(1, 3, 'A', 0))),
]))


# Small, hand-picked cases catch common geometry and coordinate mistakes.
p.add_hidden_test(TestFile([
    TestCase(1, 1, (shot(1, 1, 'Z', 0),)),
    TestCase(1, 9, (shot(1, 1, 'A', 0), shot(5, 1, 'B', 0), shot(9, 1, 'C', 0))),
    TestCase(9, 1, (shot(1, 1, 'D', 0), shot(1, 5, 'E', 0), shot(1, 9, 'F', 0))),
    # Radius 2 distinguishes a Euclidean disk from a square or Manhattan diamond.
    TestCase(5, 5, (shot(3, 3, 'R', 2),)),
    # Non-square dimensions expose swapped row/column coordinates.
    TestCase(4, 9, (shot(2, 2, 'A', 1), shot(7, 3, 'B', 1), shot(5, 2, 'C', 0))),
    TestCase(9, 4, (shot(2, 2, 'D', 1), shot(3, 7, 'E', 1), shot(2, 5, 'F', 0))),
    # Later shots must replace earlier colors only where they overlap.
    TestCase(9, 9, (shot(5, 5, 'A', 4), shot(3, 5, 'B', 2), shot(7, 5, 'C', 2), shot(5, 5, 'D', 0))),
]), 'geometry_edges')


def many_tiny_cases() -> TestFile:
    """Exercise the maximum number of test cases and paintballs."""
    return TestFile(
        TestCase(1, 1, (shot(1, 1, chr(ord('A') + i % 26), 0),))
        for i in range(MAX_T)
    )


p.add_hidden_test(many_tiny_cases, 'many_tiny_cases')


def many_overwrites() -> TestFile:
    """Maximum Q on a near-maximum grid, including repeated locations."""
    rows, cols = 316, 316  # 99,856 cells
    balls = []
    for i in range(MAX_Q):
        x = 1 + (i * 37) % cols
        y = 1 + (i * 53) % rows
        balls.append(shot(x, y, chr(ord('A') + i % 26), 0))
    return TestFile([TestCase(rows, cols, tuple(balls))])


p.add_hidden_test(many_overwrites, 'many_overwrites')


def large_disks() -> TestFile:
    """Large overlapping disks make per-cell-per-shot simulations expensive."""
    rows = cols = 316
    balls = [shot(158, 158, 'A', 157)]
    for i in range(299):
        radius = random.randint(40, 120)
        x = random.randint(radius + 1, cols - radius)
        y = random.randint(radius + 1, rows - radius)
        balls.append(shot(x, y, chr(ord('B') + i % 25), radius))
    return TestFile([TestCase(rows, cols, tuple(balls))])


p.add_hidden_test(large_disks, 'large_disks')


def maximum_radius_circles(rows: int, cols: int, q: int) -> TestCase:
    """Use only the largest radius that fits in this grid.

    Cycle through every center that permits that radius.  On an even-sized
    square there are four such centers; on an odd-sized square there is one.
    Either way, the circles overlap heavily by design.
    """
    radius = (min(rows, cols) - 1) // 2
    valid_xs = range(radius + 1, cols - radius + 1)
    valid_ys = range(radius + 1, rows - radius + 1)
    centers = [(x, y) for y in valid_ys for x in valid_xs]
    balls = [
        shot(*centers[i % len(centers)], chr(ord('A') + i % 26), radius)
        for i in range(q)
    ]
    return TestCase(rows, cols, tuple(balls))


# Maximize both the circle radius for the board and the number of shots.
# Each entry is its own input file, so each independently meets the global
# 100,000-cell and 10,000-shot limits.
for name, (rows, cols) in {
    'max_radius_square': (316, 316),
    'max_radius_wide': (100, 1000),
    'max_radius_tall': (1000, 100),
    'max_radius_very_wide': (5, 20_000),
    'max_radius_very_tall': (20_000, 5),
}.items():
    p.add_hidden_test(
        lambda rows=rows, cols=cols: TestFile([maximum_radius_circles(rows, cols, MAX_Q)]),
        name,
    )


def skinny(rows: int, cols: int, q: int) -> TestCase:
    """Skinny board where shots use the max allowed radius half the time."""
    balls = []
    for i in range(q):
        x = random.randint(1, cols)
        y = random.randint(1, rows)
        max_r = min(x - 1, cols - x, y - 1, rows - y)
        r = max_r if random.random() < 0.5 else random.randint(0, max_r)
        balls.append(shot(x, y, chr(ord('A') + i % 26), r))
    return TestCase(rows, cols, tuple(balls))

for name, (r, c) in {
    'wide_1xN': (1, 100_000),
    'tall_Nx1': (100_000, 1),
    'wide_2xN': (2, 50_000),
    'tall_Nx2': (50_000, 2),
    'wide_3xN': (3, 33_333),
    'tall_Nx3': (33_333, 3),
    'wide_5xN': (5, 20_000),
    'tall_Nx5': (20_000, 5),
}.items():
    p.add_hidden_test(
        (lambda r=r, c=c: TestFile([skinny(r, c, MAX_Q)])), name
    )

def tall_wide_big_disks() -> TestFile:
    cases = [
        skinny(50, 1000, 3000),
        skinny(1000, 49, 3000),
        TestCase(1, 1, (shot(1, 1, 'A', 0),)),
        TestCase(3, 3, (shot(2, 2, 'B', 1), shot(2, 2, 'C', 0))),
    ]
    return TestFile(cases)

p.add_hidden_test(tall_wide_big_disks, 'tall_wide_mixed')

@p.hidden_test_generator(test_count=4)
def random_medium() -> TestFile:
    """Mixed rectangular grids and circles; every file stays within global sums."""
    cases = []
    remaining_cells = MAX_CELLS
    remaining_q = MAX_Q
    while remaining_cells >= 100 and remaining_q >= 10 and len(cases) < 12:
        max_rows = min(80, remaining_cells // 10)
        rows = random.randint(10, max_rows)
        max_cols = min(160, remaining_cells // rows)
        if max_cols < 10:
            break
        cols = random.randint(10, max_cols)
        q = random.randint(10, min(150, remaining_q))
        cases.append(random_case(rows, cols, q))
        remaining_cells -= rows * cols
        remaining_q -= q
    return TestFile(cases)

def main():
    run_cli(p)

if __name__ == '__main__':
    main()
