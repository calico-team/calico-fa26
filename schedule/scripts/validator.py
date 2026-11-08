MAX_CHAIN = 900


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

    # depth[v] = number of tasks on the prerequisite chain ending at v
    # (a task with no prerequisite has depth 1). 0 means not yet computed.
    depth = [0] * (N + 1)
    for task in range(1, N + 1):
        path = []
        on_path = set()
        while task != 0 and depth[task] == 0:
            assert task not in on_path
            on_path.add(task)
            path.append(task)
            task = P[task - 1]
        d = depth[task] if task != 0 else 0
        for v in reversed(path):
            d += 1
            depth[v] = d
        # Keeps the recursive DFS in sol.py under Python's recursion limit.
        assert d <= MAX_CHAIN
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
