import heapq

def solve(N, M, K, P):
    h = [-1 for _ in range(N)]
    ins = [False for _ in range(N)]
    adj = [[] for _ in range(N)]
    for i in range(N):
        P[i] -= 1
        if P[i] != -1:
            adj[P[i]].append(i)
    def dfs(x):
        h[x] = 0
        for nxt in adj[x]:
            dfs(nxt)
            h[x] = max(h[x], h[nxt] + 1)
    pq = []
    for i in range(N):
        if P[i] == -1:
            dfs(P[i])
            heapq.heappush(pq, (-h[i], i))
    ans = 0
    for i in range(M):
        add = []
        taken = 0
        while taken < K and not len(pq) == 0:
            ans += 1
            taken += 1
            _, x = heapq.heappop(pq)
            for nxt in adj[x]:
                add.append(nxt)
        for x in add:
            heapq.heappush(pq, (-h[x], x))
    return ans

def main():
    T = int(input())
    for _ in range(T):
        N, M, K = list(map(int, input().split()))
        P = list(map(int, input().split()))
        print(solve(N, M, K, P))

if __name__ == '__main__':
    main()