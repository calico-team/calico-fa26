def solve(N: int, M: int, Q: int, G: list[str], start: list[tuple[int, int]], end: list[tuple[int, int]]) -> list[str]:
    assert 1 <= N <= 200
    assert 1 <= M <= 200
    assert 1 <= Q <= 1000

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
        
    return []


def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N, M, Q = map(int, input().split())
        G = []
        for _ in range(N):
            G.append(input())
        start, end = [], []
        for _ in range(Q):
            start_row, start_col, end_row, end_col = map(int, input().split())
            start.append((start_row, start_col))
            end.append((end_row, end_col))
        print(solve(N, M, Q, G, start, end))

if __name__ == '__main__':
    main()
