def solve_phase1(N: int, E: list[tuple[int, int]]) -> list[int]:
    """
    Phase 1: encode the tree.

    N: the number of vertices
    E: the N - 1 edges of the tree as (u, v) pairs, in arbitrary
       order — not necessarily lexicographically increasing, and u is
       not guaranteed to be the parent of v
    Returns: the N integers A_1..A_N, your encoding of the tree
    """
    # YOUR CODE HERE
    return [0] * N


def solve_phase2(N: int, A: list[int]) -> list[tuple[int, int]]:
    """
    Phase 2: recover the tree from your own encoding.

    N: the number of vertices
    A: the N integers A_1..A_N — identical to what your phase 1 output
       for this test case, with exactly one value replaced by -1 (the
       erased value)
    Returns: the N - 1 edges of the original tree as (u, v) pairs, one
             edge per output line (the checker compares the set of
             edges, so the order and orientation of the pairs do not
             matter)
    """
    # YOUR CODE HERE
    return []


def main():
    phase = input()
    N = int(input())
    if phase == 'FIRST':
        E = []
        for _ in range(N - 1):
            u, v = map(int, input().split())
            E.append((u, v))
        A = solve_phase1(N, E)
        print(' '.join(map(str, A)))
    else:
        A = list(map(int, input().split()))
        for u, v in solve_phase2(N, A):
            print(u, v)


if __name__ == '__main__':
    main()
