def solve(N: int, M: int, Q: int, G: list[str], start: list[tuple[int, int]], end: list[tuple[int, int]], K: list[int]) -> list[str]:
    assert 1 <= N <= 10
    assert 1 <= M <= 4000
    assert 1 <= Q <= 10**5

    assert len(G) == N
    for row in G:
        assert len(row) == M
        for char in row:
            assert char in ['R', 'B', '.']

    assert len(start) == Q
    for start_row, start_col in start:
        assert 0 <= start_row < N
        assert 0 <= start_col < M
        assert G[start_row][start_col] == '.'
    assert len(end) == Q
    for end_row, end_col in end:
        assert 0 <= end_row < N
        assert 0 <= end_col < M
    assert len(K) == Q
    for k in K:
        assert 0 <= k <= 10**9
        
    return []


def main():
    T = int(input())
    assert 1 <= T <= 100
    total_cells = 0
    total_queries = 0
    for _ in range(T):
        N, M, Q = map(int, input().split())
        total_cells += N * M
        assert total_cells <= 4 * 10**4
        total_queries += Q
        assert total_queries <= 10**5
        G = []
        for _ in range(N):
            G.append(input())
        start, end, K = [], [], []
        for _ in range(Q):
            start_row, start_col, end_row, end_col, k = map(int, input().split())
            start.append((start_row, start_col))
            end.append((end_row, end_col))
            K.append(k)
        print(solve(N, M, Q, G, start, end, K))

if __name__ == '__main__':
    main()
