import sys
sys.setrecursionlimit(5000)

seen = set()

def dfs(adj, u, parent):
    assert u not in seen, f'seen {seen}, currently at {u}'
    seen.add(u)

    for neighbor in adj[u]:
        if neighbor != parent:
            dfs(adj, neighbor, u)

def main():
    PHASE = input()
    assert PHASE == "FIRST"

    N = int(input())
    assert 2 <= N <= int(2e5)

    e = [[] for i in range(N + 1)]
    for i in range(N - 1):
        p, c = map(int, input().split(" "))
        assert 1 <= p <= N
        assert 1 <= c <= N

        e[p].append(c)
        e[c].append(p)
        
    dfs(e, 1, 0)

    expected = set(range(1, N + 1))
    assert seen == expected, f'seen does not match expected: {seen}'
            


if __name__ == '__main__':
    main()
