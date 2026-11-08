#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 1e5, N <= 2e5, 0 <= Li <= Ri < 2^(30)

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
solution = cpp_runner(
    os.path.join(problem_dir, 'submissions/accepted/matcha.cpp'),
    os.path.join(problem_dir, 'matcha.bin'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'matcha',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=4, time_limit=2),
    ],
    solution=solution,
    seed='matchaaaaaaa')

class TestCase(NamedTuple):
    N: int 
    L: list[int]
    R: list[int]

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
            lines.append(f'{case.N}')
            lines.append(' '.join(map(str, case.L)))
            lines.append(' '.join(map(str, case.R)))
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(1, [6], [7]),
    TestCase(3, [0, 0, 0], [1073741823, 1073741823, 1073741823]),
    TestCase(4, [0, 1, 3, 5], [1, 2, 4, 8]),
    TestCase(3, [98, 98, 101], [105, 103, 110])
]))

# Hidden tests are secret (not shown to contestants).

# A hard-coded test is just an explicit list of cases.
p.add_hidden_test(TestFile([
    TestCase(23, [79691776, 24379392, 260308992, 0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287], [243269632, 71565312, 265027584, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]),
    TestCase(26, [3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431, 67108863, 89478483], [6, 10, 18, 34, 66, 130, 258, 514, 1026, 2050, 4098, 8194, 16386, 32770, 65538, 131074, 262146, 524290, 1048578, 2097154, 4194306, 8388610, 16777218, 33554434, 67108866, 89478483])
]), "anti_cheese")

# Anything built from a loop or ``random`` should be a factory, not an
# instance: the factory runs after the library has seeded ``random``.

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=1)
def brute_force() -> TestFile:
    test = TestFile([])
    for one in range(16):
        for two in range(16):
            for three in range(16):
                for four in range(16):
                    L = [one // 4, two // 4, three // 4, four // 4]
                    R = [one % 4, two % 4, three % 4, four % 4]
                    bad = False
                    for i in range(4):
                        if L[i] > R[i]:
                            bad = True
                    if not bad:
                        test.cases.append(TestCase(4, L, R))
    return test

@p.hidden_test_generator(test_count=4)
def pure_random_2() -> TestFile:
    test = TestFile([])
    for _ in range(100000):
        N = 2
        L = []
        R = []
        for i in range(N):
            L.append(random.randint(0, (1 << 30) - 1))
            R.append(random.randint(L[-1], (1 << 30) - 1))
        test.cases.append(TestCase(N, L, R))
    return test

@p.hidden_test_generator(test_count=4)
def pure_random_3() -> TestFile:
    test = TestFile([])
    for _ in range(66666):
        N = 3
        L = []
        R = []
        for i in range(N):
            L.append(random.randint(0, (1 << 30) - 1))
            R.append(random.randint(L[-1], (1 << 30) - 1))
        test.cases.append(TestCase(N, L, R))
    return test

@p.hidden_test_generator(test_count=1)
def pure_random_200000() -> TestFile:
    test = TestFile([])
    N = random.randint(150000, 200000)
    L = []
    R = []
    for i in range(N):
        L.append(random.randint(0, (1 << 30) - 1))
        R.append(random.randint(L[-1], (1 << 30) - 1))
    test.cases.append(TestCase(N, L, R))
    return test

import subprocess
B = 30
MAXV = (1 << B) - 1

def all_ones_cap(R):
    """The trivial answer: all ones up to the top bit of OR(R)."""
    o = 0
    for r in R:
        o |= r
    return (1 << o.bit_length()) - 1
 
def ref_answers(cases):
    """Run the compiled reference on a list of TestCase; return the answers."""
    inp = [str(len(cases))]
    for c in cases:
        inp += [str(c.N), ' '.join(map(str, c.L)), ' '.join(map(str, c.R))]
    out = subprocess.run([os.path.join(problem_dir, 'matcha.bin')],
                         input='\n'.join(inp) + '\n',
                         capture_output=True, text=True, check=True).stdout
    return list(map(int, out.split()))
 
def shuffled_case(L, R):
    idx = list(range(len(L)))
    random.shuffle(idx)
    return TestCase(len(L), [L[i] for i in idx], [R[i] for i in idx])
 
def split_sizes(total, T, mn=3):
    """Random sizes for T cases summing to total, each at least mn."""
    extra = total - mn * T
    cuts = sorted(random.randint(0, extra) for _ in range(T - 1))
    return [mn + y - x for x, y in zip([0] + cuts, cuts + [extra])]


def straddle_case(n):
    """
    Narrow intervals that cross an odd multiple of 2^k at a few high levels k,
    so high bits are real choices that pin the low bits; the rest is narrow
    filler that never crosses a 2^g0 boundary. Rerolls if the answer is all ones.
    """
    while True:
        wmax = random.randint(2, 8)                       # widths < 2^wmax
        g0 = min(B - 2, wmax + random.randint(1, 4))      # filler stays inside 2^g0 blocks
        K = random.sample(range(g0, B), min(random.randint(2, 6), B - g0))
        L, R = [], []
        for k in K:                                       # straddlers at level k
            for _ in range(random.choice([1, 1, 2, 3, 5, 20, 200])):
                if len(L) >= n:
                    break
                X = random.randrange(1, 1 << (B - k), 2) << k   # odd multiple of 2^k
                L.append(max(0, X - random.randint(1, 1 << wmax)))
                R.append(min(MAXV, X + random.randint(1, 1 << wmax) - 1))
        while len(L) < n:                                 # filler
            w = random.randint(0, (1 << random.randint(0, wmax)) - 1)
            q = random.randrange(1 << (B - g0))
            lo = random.randrange((1 << g0) - w)
            L.append((q << g0) | lo)
            R.append((q << g0) | (lo + w))
        case = shuffled_case(L, R)
        if ref_answers([case])[0] != all_ones_cap(case.R):
            return case
 
@p.hidden_test_generator(test_count=3)
def straddle_large() -> TestFile:
    """One case with N = 2e5."""
    return TestFile([straddle_case(200000)])
 
@p.hidden_test_generator(test_count=2)
def straddle_multi() -> TestFile:
    """50 cases with random sizes summing to 2e5."""
    return TestFile([straddle_case(n) for n in split_sizes(200000, 50)])


def main():
    # Run cli (try `python main.py --help`)
    run_cli(p)

    # Can also specify actions
    # p.init_problem()
    # p.create_all_tests()
    # p.create_zip()

if __name__ == '__main__':
    main()
