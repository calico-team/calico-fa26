def solve_phase1(N: int, P: list[int]) -> list[int]:
    """
    Phase 1: encode the tree.

    N: the number of vertices
    P: the parent array of the tree: P[i] is the parent of vertex i + 1,
       or i + 1 if vertex i + 1 has no parent (the root).
    Returns: the N integers A_1..A_N, your encoding of the tree.
    """
    # YOUR CODE HERE
    return [0] * N


def solve_phase2(N: int, A: list[int]) -> list[int]:
    """
    Phase 2: recover the tree from your own encoding.

    N: the number of vertices
    A: the N integers A_1..A_N — identical to what your phase 1 output
       for this test case, with exactly one value replaced by -1 (the
       erased value).
    Returns: the N integers P_1..P_N, the parent array of the original
             tree (P[i] is the parent of vertex i + 1, or i + 1 if
             vertex i + 1 has no parent).
    """
    # YOUR CODE HERE
    return [0] * N


def main():
    T, phase = map(int, input().split())
    for _ in range(T):
        N = int(input())
        if phase == 1:
            P = list(map(int, input().split()))
            A = solve_phase1(N, P)
        else:
            A = list(map(int, input().split()))
            P = solve_phase2(N, A)
        print(' '.join(map(str, A if phase == 1 else P)))


if __name__ == '__main__':
    main()
