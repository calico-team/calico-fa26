#!/usr/bin/env python3

import sys


MAX_T = 10_000          # 1 <= T
MAX_CELLS = 1_000_000     # N * M per case, AND sum of N * M across a file
MAX_Q = 10_000          # Q per case, AND sum of Q across a file



def main() -> None:
    tokens = sys.stdin.read().split()
    it = iter(tokens)
    t = int(next(it))
    assert 1 <= t <= MAX_T
    total_cells = total_q = 0

    for _ in range(t):
        n, m, q = int(next(it)), int(next(it)), int(next(it))
        assert n >= 1 and m >= 1 and q >= 1
        total_cells += n * m
        total_q += q
        assert total_cells <= MAX_CELLS
        assert total_q <= MAX_Q
        for _ in range(q):
            x, y, radius = int(next(it)), int(next(it)), int(next(it))
            assert radius >= 0
            assert 1 + radius <= x <= m - radius
            assert 1 + radius <= y <= n - radius

    try:
        next(it)
        assert False, 'extra input'
    except StopIteration:
        pass


if __name__ == '__main__':
    main()
