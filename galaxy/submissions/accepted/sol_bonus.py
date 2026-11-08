class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connect(self, a: int, b: int) -> bool:
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def isConnected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

def solve(N: int, M: int, Q: int, G: list[str], start: list[tuple[int, int]], end: list[tuple[int, int]]) -> list[str]:
    dsu = DSU(N * M)
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    for row in range(N):
        for col in range(M):
            for dr, dc in dirs:
                if row+dr >= 0 and row+dr < N and col+dc >= 0 and col+dc < M:
                    cur, nxt = G[row][col], G[row+dr][col+dc]
                    if cur == nxt or cur == "." or nxt == ".":
                        dsu.connect(row*M+col, (row+dr)*M+(col+dc))
    ans = []
    for (start_row, start_col), (end_row, end_col) in zip(start, end):
        ans.append("YES" if dsu.isConnected(start_row*M+start_col, end_row*M+end_col) else "NO")
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
