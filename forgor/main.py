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

problem_dir = os.path.dirname(__file__)

validator = py_runner(os.path.join(problem_dir, 'scripts/validator.py'))
validator_main = py_runner(os.path.join(problem_dir, 'scripts/validator_main.py'))

p = Problem(
    'forgor',
    problem_dir,
    test_sets=[
        Subproblem('main', rank=3),
    ],
    solution=None,
    seed='did i really just forget that melody')

class TestCase(NamedTuple):
    N: int
    E: list[tuple[int, int]]
    R: int # index of value that will be erased in phase 2

@p.pre_gen_fn
def pre_gen_fn():
    """Compile the cpp solution once before generation (the library won't)."""
    pass

class TestFile(TestFileBase):
    def __init__(self, cases: Iterable[TestCase]) -> None:
        self.cases = list(cases)
        super().__init__()

    @override
    def write_test_in(self) -> str:
        lines = ["FIRST"]

        assert len(self.cases) == 1, f'More than 1 test case found in test file'
        for case in self.cases:
            lines.append(f'{case.N}')
            for i in range(case.N - 1):
                lines.append(' '.join(map(str, case.E[i])))
        return '\n'.join(lines) + '\n'

    @override
    def write_test_out(self, infile: str) -> str:
        case = self.cases[0]
        lines = [str(case.R)]

        for i in range(case.N - 1):
            lines.append(' '.join(map(str, case.E[i])))

        return '\n'.join(lines) + '\n'

    @override
    def validate_test_in(self, infile: str) -> None:
        """Run the validators against the input written at ``infile``."""
        validator_main.exec_file(infile)

# Sample tests are shown to contestants; added to all subproblems by default.
p.add_sample_test(TestFile([
    TestCase(3, [(1, 2), (1, 3)], 0)
]))

def generate_tree_dfs(N, branch_factor=8):
    available_nodes = list(range(1, N + 1))
    random.shuffle(available_nodes)
    edges = []

    root = available_nodes.pop()
    path = [root]

    while available_nodes and path:
        parent = path.pop() 

        max_children = max(1, len(available_nodes) // branch_factor)
        num_children = min(len(available_nodes), random.randint(1, max_children) )

        nodes = []
        for _ in range(num_children):
            node = available_nodes.pop()
            nodes.append(node)
            edges.append((parent, node))

        path.extend(nodes)

    while available_nodes:
        edges.append((root, available_nodes.pop()))

    return edges

def generate_tree_bfs(N, branch_factor=8):
    nodes = list(range(1, N + 1))
    random.shuffle(nodes)
    
    edges = []
    parent_queue = [nodes[0]]
    queue_idx = 0
    next_node_idx = 1
    
    while next_node_idx < N and queue_idx < len(parent_queue):
        parent = parent_queue[queue_idx]
        queue_idx += 1
        
        remaining = N - next_node_idx
        max_children = max(1, remaining // branch_factor)
        num_children = min(remaining, random.randint(1, max_children))
        
        for _ in range(num_children):
            child = nodes[next_node_idx]
            edges.append((parent, child))
            parent_queue.append(child)
            next_node_idx += 1
            
    while next_node_idx < N:
        edges.append((random.choice(nodes[:next_node_idx]), nodes[next_node_idx]))
        next_node_idx += 1
        
    return edges

# Aldous-Broder algorithm (?!)
def generate_tree_uniform(N):
    edges = []
    visited = {random.randint(1, N)}
    current = next(iter(visited))

    while len(visited) < N:
        neighbor = random.randint(1, N)
        if neighbor not in visited:
            visited.add(neighbor)
            edges.append((current, neighbor))
        current = neighbor

    return edges

# Random tests are factories too, for the same seeding reason.
@p.hidden_test_generator(test_count=5)
def pure_random_dfs() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])

    N = random.randint(2, int(2e5))
    tree = []
    while not tree:
        tree = generate_tree_dfs(N)
    R = random.randint(0, N - 1)
    test.cases.append(TestCase(N, tree, R))
    return test

@p.hidden_test_generator(test_count=5)
def pure_random_bfs() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])

    N = random.randint(2, int(2e5))
    tree = []
    while not tree:
        tree = generate_tree_bfs(N)
    R = random.randint(0, N - 1)
    test.cases.append(TestCase(N, tree, R))
    return test

@p.hidden_test_generator(test_count=10)
def pure_random_uniform() -> TestFile:
    """Generate a test file with 10 random cases, valid for every subproblem."""
    test = TestFile([])

    N = random.randint(2, int(2e5))
    tree = []
    while not tree:
        tree = generate_tree_uniform(N)
    R = random.randint(0, N - 1)
    test.cases.append(TestCase(N, tree, R))
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
