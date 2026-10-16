def solve(N: int, M: int, G: list[str]) -> str:
    stack = [(0,0)]
    visited = [[False] * M for _ in range(N)]
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    while stack:
        row, col = stack.pop()
        if row == N-1 and col == M-1:
            return "YES"
        for dr, dc in dirs:
            if row+dr >= 0 and row+dr < N and col+dc >= 0 and col+dc < M:
                cur, nxt = G[row][col], G[row+dr][col+dc]
                if not visited[row+dr][col+dc] and (cur == nxt or cur == "." or nxt == "."):
                    visited[row+dr][col+dc] = True
                    stack.append((row+dr, col+dc))
    return "NO"

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            G.append(input())
        print(solve(N, M, G))

if __name__ == '__main__':
    main()
