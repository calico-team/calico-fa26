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
solution = py_runner(os.path.join(problem_dir, 'scripts/generate_output.py'))
validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

# ``solution`` is run to produce every answer, so you don't need to override
# ``write_test_out``. ``seed`` is handled by the library: it calls
# ``random.seed`` before each test, so you can't forget to seed.
p = Problem(
    'forgor',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=3),
    ],
    solution=solution,
    seed='did i really just forget that melody')

class TestCase(NamedTuple):
    N: int
    P: list[int]

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
        lines = [str(len(self.cases)) + " 1"]
        for case in self.cases:
            lines.append(f'{case.N}')
            lines.append(' '.join(map(str, case.P)))
        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(3, [2, 1, 2])
]))

# Iterative DFS-like random tree generation
def generate_tree(N):
    available_nodes = list(range(1, N + 1))
    parent = [-1] * N

    root = random.choice(available_nodes)
    parent[root - 1] = root
    available_nodes.remove(root)

    path = [root]
    while available_nodes and path:
        num_children = random.randint(0, max(1, len(available_nodes) // 8)) 
        if num_children == 0:
            path.pop()
            continue

        nodes = []
        for i in range(num_children):
            node = random.choice(available_nodes)
            nodes.append(node)
            available_nodes.remove(node)
            parent[node - 1] = path[-1]

        path.extend(nodes)

    return [] if available_nodes else parent

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=4)
def pure_random() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])
    for _ in range(10):
        N = random.randint(2, 1023)
        tree = []
        while not tree:
            tree = generate_tree(N)
        test.cases.append(TestCase(N, tree))
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
