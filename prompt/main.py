#!/usr/bin/env python3

# Example add problem.
# Constraints:
#   main: T <= 100, A <= 100, B <= 100
#   bonus: T <= 1e5, A <= 1e12, B <= 1e12

import os
import random
from collections.abc import Iterable
from typing import NamedTuple, override
import string

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
    os.path.join(problem_dir, 'submissions/accepted/prompt.cpp'),
    os.path.join(problem_dir, 'prompt.bin'))
#solution = py_runner(os.path.join(problem_dir, 'submissions/accepted/prompt.py'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'prompt',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=1),
    ],
    solution=solution,
    seed='build me a billion dollar startup. make no mistakes.')

class TestCase(NamedTuple):
    S: str

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
            lines.append(f'{case.S}')
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        # main has tighter constraints (A, B <= 100).
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase("can_you_write_me_a_rank_1_"),
    TestCase("solve_all_of_the_rank_4_problems_"),
    TestCase("what_is_the_day_gta6_comes_out_"),
    TestCase("what_is_gg_ez_"),
    TestCase("bye_super_intelligence_")
]))

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    """Generate a test file with 100 random cases, valid for every subproblem."""
    letters = string.ascii_lowercase + string.digits + "_"
    patterns = ["write_me", "what_is", "solve", ""]

    test = TestFile([])
    for _ in range(100):
        start_len = random.randint(0, 40)
        end_len = random.randint(0, 40)
        start = ''.join(random.choices(letters, k=start_len))
        end = ''.join(random.choices(letters, k=end_len))

        pattern = random.choice(patterns)
        test.cases.append(TestCase(start + pattern + end + "_"))
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
