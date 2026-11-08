from collections import deque

def solve(N: int, M: int, Q: int, G: list[str], start: list[tuple[int, int]], end: list[tuple[int, int]]) -> list[str]:
    queue = deque([(N-1, M-1)])
    visited = [[False] * M for _ in range(N)]
    visited[N-1][M-1] = True
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    while queue:
        row, col = queue.popleft()
        for dr, dc in dirs:
            if row+dr >= 0 and row+dr < N and col+dc >= 0 and col+dc < M:
                cur, nxt = G[row][col], G[row+dr][col+dc]
                if not visited[row+dr][col+dc] and (cur == nxt or cur == "." or nxt == "."):
                    visited[row+dr][col+dc] = True
                    queue.append((row+dr, col+dc))

    ans = []
    for start_row, start_col in start:
        ans.append("YES" if visited[start_row][start_col] else "NO")
    return ans

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
        for s in solve(N, M, Q, G, start, end):
            print(s)

if __name__ == '__main__':
    main()
