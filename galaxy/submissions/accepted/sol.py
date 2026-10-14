def solve(N: int, M: int, G: list[str]) -> str:
    stack = [(0,0)]
    dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]
    while stack:
        row, col = stack.pop()
        if row == N and col == M:
            return "YES"
        for dr, dc in dirs:
            if row+dr >= 0 and row+dr < N and col+dc >= 0 and col+dc < M:
                cur, nxt = G[row][col], G[row+dr][col+dc]
                if cur == nxt or cur == "." or nxt == ".":
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