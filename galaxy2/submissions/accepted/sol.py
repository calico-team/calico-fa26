from collections import deque

def solve(N: int, M: int, Q: int, G: list[str], start: list[tuple[int, int]], end: list[tuple[int, int]], K: list[int]) -> list[str]:
    INF = 1 << 30
    row = [i // M for i in range(N * M)]
    col = [i % M for i in range(N * M)]
    flat = ''.join(G)
    is_dot = [ch == '.' for ch in flat]
    can_stand = [[ch != 'B' for ch in flat], [ch != 'R' for ch in flat]]
    neighbors = [[] for _ in range(N * M)]
    for i in range(N * M):
        if row[i] > 0:
            neighbors[i].append(i - M)
        if row[i] < N - 1:
            neighbors[i].append(i + M)
        if col[i] > 0:
            neighbors[i].append(i - 1)
        if col[i] < M - 1:
            neighbors[i].append(i + 1)

    dist = [INF] * (N * M * 2)
    ans = [2 * INF] * Q
    start_id = [(r * M + c) * 2 + 1 for r, c in start]
    end_id = [(r * M + c) * 2 for r, c in end]

    def bfs(r0, r1, c0, c1, source):
        width = (c1 - c0 + 1) * 2
        for r in range(r0, r1 + 1):
            first = (r * M + c0) * 2
            dist[first:first + width] = [INF] * width
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            d = dist[u] + 1
            cell, s = u // 2, u % 2
            if is_dot[cell] and dist[u ^ 1] == INF:
                dist[u ^ 1] = d
                queue.append(u ^ 1)
            for v in neighbors[cell]:
                if can_stand[s][v] and r0 <= row[v] <= r1 and c0 <= col[v] <= c1 and dist[v * 2 + s] == INF:
                    dist[v * 2 + s] = d
                    queue.append(v * 2 + s)

    def divide(r0, r1, c0, c1, qs):
        if r0 > r1 or c0 > c1 or not qs:
            return
        split_col = c1 - c0 >= r1 - r0
        if split_col:
            mid = (c0 + c1) // 2
            sep = [(r * M + mid) * 2 + s for r in range(r0, r1 + 1) for s in range(2)]
        else:
            mid = (r0 + r1) // 2
            sep = [(mid * M + c) * 2 + s for c in range(c0, c1 + 1) for s in range(2)]

        queries_from = {}
        for q in qs:
            queries_from.setdefault(start_id[q], []).append(q)

        for source in sep:
            if not can_stand[source % 2][source // 2]:
                continue
            bfs(r0, r1, c0, c1, source)
            for u, group in queries_from.items():
                if dist[u] < INF:
                    for q in group:
                        e = end_id[q]
                        ans[q] = min(ans[q], dist[u] + min(dist[e], dist[e + 1]))

        first, second = [], []
        for q in qs:
            a = start[q][1] if split_col else start[q][0]
            b = end[q][1] if split_col else end[q][0]
            if a < mid and b < mid:
                first.append(q)
            if a > mid and b > mid:
                second.append(q)
        if split_col:
            divide(r0, r1, c0, mid - 1, first)
            divide(r0, r1, mid + 1, c1, second)
        else:
            divide(r0, mid - 1, c0, c1, first)
            divide(mid + 1, r1, c0, c1, second)

    divide(0, N - 1, 0, M - 1, list(range(Q)))
    return ['YES' if ans[q] <= K[q] else 'NO' for q in range(Q)]

def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N, M, Q = map(int, input().split())
        G = []
        for _ in range(N):
            G.append(input())
        start, end, K = [], [], []
        for _ in range(Q):
            start_row, start_col, end_row, end_col, k = map(int, input().split())
            start.append((start_row, start_col))
            end.append((end_row, end_col))
            K.append(k)
        for s in solve(N, M, Q, G, start, end, K):
            print(s)

if __name__ == '__main__':
    main()
