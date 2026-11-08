def solve(N: int, M: int, K: int, P: list[int]) -> int:
    """
    Validate one test case. P[i] is the 1-indexed prerequisite of task i+1,
    or 0 if it has none.
    """
    assert 1 <= N <= 10000
    assert 1 <= M <= 50000
    assert 1 <= K <= N
    assert len(P) == N
    for p in P:
        assert 0 <= p <= N

    reaches_root = {0}
    for task in range(1, N + 1):
        path = set()
        while task not in reaches_root:
            assert task not in path
            path.add(task)
            task = P[task - 1]
        reaches_root |= path
    return 0


def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N, M, K = map(int, input().split())
        P = list(map(int, input().split()))
        solve(N, M, K, P)

if __name__ == '__main__':
    main()
