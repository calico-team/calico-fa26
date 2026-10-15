def solve(N: int, M: int, G: list[str]) -> int:
    assert 1 <= N <= 1000
    assert 1 <= M <= 1000
    assert G[0][0] in ['B', '.']
    assert len(G) == N
    for row in G:
        assert len(row) == M
        for char in row:
            assert char in ['R', 'B', '.']
    return 0


def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            G.append(input())
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
