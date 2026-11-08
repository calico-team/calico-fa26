#!/usr/bin/env python3

import os
import random
from collections.abc import Iterable
from math import isqrt
from typing import NamedTuple, override

from calico_lib import Problem, Subproblem, TestFileBase, cpp_runner, py_runner, run_cli



# this is claude's translation/update of the cases for the older version (color chars) to be for the new version


# 1 <= T
# N * M per case, AND sum of N * M across a file
# Q per case, AND sum of Q across a file
MAX_T = 10_000
MAX_CELLS = 1_000_000
MAX_Q = 20_000

NEAR_MAX_JITTER = 3             # "near-max" power is max_power - randint(0, this)
SMALL_POWER_CAP = 5             # power cap for the "small quakes on a big grid" test
ASPECT_RATIOS = (4, 100)        # long side / short side for the rectangular max-size tests
RANDOM_MAX_CASES = 30           # cases per random_medium file
RANDOM_TEST_COUNT = 2           # number of random_medium files

# ---------------------------------------------------------------------------
# Problem setup.
# ---------------------------------------------------------------------------
PROBLEM_NAME = 'shock'
SOLUTION_NAME = 'shock_implicit_dsu_sol'

problem_dir = os.path.dirname(__file__)
solution = cpp_runner(
    os.path.join(problem_dir, f'submissions/accepted/{SOLUTION_NAME}.cpp'),
    os.path.join(problem_dir, f'{SOLUTION_NAME}.bin'),
)
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

p = Problem(
    PROBLEM_NAME,
    problem_dir,
    test_sets=[
        Subproblem('main', rank=3, time_limit=4) #, mem_limit=100_000_000)
    ],
    solution=solution,
    seed='shock_seed_678128904567890',
)


# ---------------------------------------------------------------------------
# Data model.  Coordinates: x = column in [1, M], y = row in [1, N].
# ---------------------------------------------------------------------------
class Quake(NamedTuple):
    x: int      # column of epicenter
    y: int      # row of epicenter
    power: int


class TestCase(NamedTuple):
    rows: int   # N
    cols: int   # M
    quakes: tuple[Quake, ...]


def check_limits(cases: list[TestCase]) -> None:
    """Fail fast (before running the solution) if a generator breaks a constraint."""
    if not 1 <= len(cases) <= MAX_T:
        raise ValueError(f'T={len(cases)} out of range')
    if sum(c.rows * c.cols for c in cases) > MAX_CELLS:
        raise ValueError('sum of N*M exceeds MAX_CELLS')
    if sum(len(c.quakes) for c in cases) > MAX_Q:
        raise ValueError('sum of Q exceeds MAX_Q')
    for c in cases:
        if not 1 <= c.rows * c.cols <= MAX_CELLS:
            raise ValueError(f'bad grid {c.rows}x{c.cols}')
        if not 1 <= len(c.quakes) <= MAX_Q:
            raise ValueError(f'bad quake count {len(c.quakes)}')
        for q in c.quakes:
            if not (
                q.power >= 0
                and 1 + q.power <= q.x <= c.cols - q.power
                and 1 + q.power <= q.y <= c.rows - q.power
            ):
                raise ValueError(f'bad quake {q} in {c.rows}x{c.cols} grid')


class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        check_limits(self.cases)
        super().__init__()

    @override
    def write_test_in(self) -> str:
        lines = [str(len(self.cases))]
        for case in self.cases:
            lines.append(f'{case.rows} {case.cols} {len(case.quakes)}')
            lines.extend(f'{q.y} {q.x} {q.power}' for q in case.quakes)
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        if 'main' in self.subproblems:
            validator_main.exec_file(infile)
        validator.exec_file(infile)


# ---------------------------------------------------------------------------
# Geometry helpers.
# ---------------------------------------------------------------------------
def max_power_at(rows: int, cols: int, x: int, y: int) -> int:
    """Largest power allowed at epicenter (x, y)."""
    return min(x - 1, cols - x, y - 1, rows - y)


def max_power_in(rows: int, cols: int) -> int:
    """Largest power allowed anywhere in the grid."""
    return (min(rows, cols) - 1) // 2


def center_of(rows: int, cols: int) -> tuple[int, int]:
    """A cell (x, y) that permits max_power_in(rows, cols) (and every smaller power)."""
    return (cols + 1) // 2, (rows + 1) // 2


def max_square_side() -> int:
    return isqrt(MAX_CELLS)


def rect_shape(aspect: int) -> tuple[int, int]:
    """(rows, cols) with cols ~= aspect * rows and rows * cols <= MAX_CELLS."""
    rows = max(1, isqrt(MAX_CELLS // aspect))
    return rows, MAX_CELLS // rows


# ---------------------------------------------------------------------------
# Quake / case builders.
# ---------------------------------------------------------------------------
def random_quake(rows: int, cols: int, power_cap: int | None = None) -> Quake:
    """Uniformly random epicenter, then a random legal power at that epicenter."""
    x = random.randint(1, cols)
    y = random.randint(1, rows)
    top = max_power_at(rows, cols, x, y)
    if power_cap is not None:
        top = min(top, power_cap)
    return Quake(x, y, random.randint(0, top))


def near_max_quake(rows: int, cols: int, jitter: int) -> Quake:
    """Power within `jitter` of the grid's maximum. Because the radius is nearly
    as large as the grid allows, the epicenter is forced near the center."""
    power = max(0, max_power_in(rows, cols) - random.randint(0, jitter))
    x = random.randint(power + 1, cols - power)
    y = random.randint(power + 1, rows - power)
    return Quake(x, y, power)


def random_case(rows: int, cols: int, q: int, power_cap: int | None = None) -> TestCase:
    return TestCase(rows, cols, tuple(random_quake(rows, cols, power_cap) for _ in range(q)))


def near_max_case(rows: int, cols: int, q: int, jitter: int = NEAR_MAX_JITTER) -> TestCase:
    return TestCase(rows, cols, tuple(near_max_quake(rows, cols, jitter) for _ in range(q)))


def mixed_case(rows: int, cols: int, q: int, jitter: int = NEAR_MAX_JITTER) -> TestCase:
    """Half near-max quakes, half random quakes (shuffled together by coin flips)."""
    quakes = tuple(
        near_max_quake(rows, cols, jitter) if random.random() < 0.5 else random_quake(rows, cols)
        for _ in range(q)
    )
    return TestCase(rows, cols, quakes)


def concentric_case(rows: int, cols: int, q: int, descending: bool) -> TestCase:
    """Every quake at the same epicenter, powers sweeping between 0 and the max.
    Descending: each later quake only overwrites the inside of the previous one,
    so every quake leaves a visible ring. Ascending: each quake swallows the last."""
    top = max_power_in(rows, cols)
    x, y = center_of(rows, cols)
    quakes = []
    for i in range(q):
        step = i % (top + 1)
        quakes.append(Quake(x, y, top - step if descending else step))
    return TestCase(rows, cols, tuple(quakes))


# ---------------------------------------------------------------------------
# Tests.  File numbering follows registration order, so the max-size test
# below is intentionally registered second (right after the hand-picked one).
# ---------------------------------------------------------------------------

# Statement samples.
p.add_sample_test(TestFile([
    TestCase(5, 6, (Quake(4, 3, 2),)),
    TestCase(4, 3, (Quake(2, 2, 1), Quake(2, 3, 1), Quake(2, 3, 0))),
    TestCase(9, 9, (Quake(5, 5, 4), Quake(4, 5, 0))),
]))


# 00: small hand-picked cases for geometry / coordinate / overwrite mistakes.
p.add_hidden_test(TestFile([
    TestCase(1, 1, (Quake(1, 1, 0),)),
    # Single row / single column, power 0 only.
    TestCase(1, 9, (Quake(1, 1, 0), Quake(5, 1, 0), Quake(9, 1, 0))),
    TestCase(9, 1, (Quake(1, 1, 0), Quake(1, 5, 0), Quake(1, 9, 0))),
    # Power 2 distinguishes a Euclidean disk from a square or Manhattan diamond,
    # and touches all four edges of the grid.
    TestCase(5, 5, (Quake(3, 3, 2),)),
    # Non-square grids expose swapped row/column (x/y, N/M) mistakes.
    TestCase(4, 9, (Quake(2, 2, 1), Quake(7, 3, 1), Quake(5, 2, 0))),
    TestCase(9, 4, (Quake(2, 2, 1), Quake(3, 7, 1), Quake(2, 5, 0))),
    # Later (even weaker) quakes replace earlier readings only where they reach.
    TestCase(9, 9, (Quake(5, 5, 4), Quake(3, 5, 2), Quake(7, 5, 2), Quake(5, 5, 0))),
]), 'geometry_edges')


# 01: THE BIG ONE. Largest possible square grid, max Q, near-max-radius quakes
# that (by construction) all land around the center of the grid.
def max_square_center_spam() -> TestFile:
    side = max_square_side()
    return TestFile([near_max_case(side, side, MAX_Q)])


p.add_hidden_test(max_square_center_spam, 'max_square_center_spam')


# 02: as many test cases as the constraints allow.
def many_tiny_cases() -> TestFile:
    n_cases = min(MAX_T, MAX_Q, MAX_CELLS)
    cells_each = MAX_CELLS // n_cases
    q_each = MAX_Q // n_cases
    cases = []
    for _ in range(n_cases):
        rows = random.randint(1, cells_each)
        cols = random.randint(1, cells_each // rows)
        cases.append(random_case(rows, cols, q_each))
    return TestFile(cases)


p.add_hidden_test(many_tiny_cases, 'many_tiny_cases')


# 03: exact maximum power only; the boundary shock levels (1) sit exactly on the grid edge.
def max_square_exact_radius() -> TestFile:
    side = max_square_side()
    return TestFile([near_max_case(side, side, MAX_Q, jitter=0)])


p.add_hidden_test(max_square_exact_radius, 'max_square_exact_radius')


# 04 / 05: all quakes share one epicenter on the largest square grid.
def concentric(descending: bool) -> TestFile:
    side = max_square_side()
    return TestFile([concentric_case(side, side, MAX_Q, descending)])


p.add_hidden_test(lambda: concentric(True), 'concentric_descending')
p.add_hidden_test(lambda: concentric(False), 'concentric_ascending')


# 06: big grid, tiny quakes: most cells are never touched, many only touched once.
def big_grid_small_quakes() -> TestFile:
    side = max_square_side()
    return TestFile([random_case(side, side, MAX_Q, power_cap=SMALL_POWER_CAP)])


p.add_hidden_test(big_grid_small_quakes, 'big_grid_small_quakes')


# 07+: max-size rectangles (wide and tall) with a mix of huge and random quakes.
for aspect in ASPECT_RATIOS:
    shape_rows, shape_cols = rect_shape(aspect)
    p.add_hidden_test(
        lambda r=shape_rows, c=shape_cols: TestFile([mixed_case(r, c, MAX_Q)]),
        f'wide_aspect_{aspect}',
    )
    p.add_hidden_test(
        lambda r=shape_rows, c=shape_cols: TestFile([mixed_case(c, r, MAX_Q)]),
        f'tall_aspect_{aspect}',
    )


# Degenerate strips: 1 x N, N x 1, N x 2, 3 x N.
STRIPS = {
    'wide_1xN': (1, MAX_CELLS),
    'tall_Nx1': (MAX_CELLS, 1),
    'tall_Nx2': (MAX_CELLS // 2, 2),
    'wide_3xN': (3, MAX_CELLS // 3),
}
for strip_name, (strip_rows, strip_cols) in STRIPS.items():
    p.add_hidden_test(
        lambda r=strip_rows, c=strip_cols: TestFile([mixed_case(r, c, MAX_Q)]),
        strip_name,
    )


# Several cases per file with random shapes; sums stay inside the global limits.
@p.hidden_test_generator(test_count=RANDOM_TEST_COUNT)
def random_medium() -> TestFile:
    cases = []
    cells_left = MAX_CELLS
    q_left = MAX_Q
    cell_scale = max(1, 2 * MAX_CELLS // RANDOM_MAX_CASES)
    q_scale = max(1, 2 * MAX_Q // RANDOM_MAX_CASES)
    while len(cases) < RANDOM_MAX_CASES and cells_left >= 1 and q_left >= 1:
        budget = min(cells_left, random.randint(1, cell_scale))
        side = isqrt(budget)
        rows = random.randint(max(1, side // 3), min(budget, 3 * side))
        per_row = budget // rows
        cols = random.randint(max(1, per_row // 2), per_row)
        q = random.randint(1, min(q_left, q_scale))
        cases.append(mixed_case(rows, cols, q))
        cells_left -= rows * cols
        q_left -= q
    return TestFile(cases)


def main():
    run_cli(p)


if __name__ == '__main__':
    main()