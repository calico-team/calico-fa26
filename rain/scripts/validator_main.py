def solve(N: int, K: int, drones: list[tuple[int, int, int, str]]) -> int:
    """
    The drone represents (X, Y, Z, D).
    """
    assert 1 <= N <= 10**5
    assert 1 <= K <= 10**9
    assert len(drones) == N
    
    position = set()
    for X, Y, Z, D in drones:
        assert 0 <= X <= 10**5
        assert 0 <= Y <= 10**5
        assert 0 <= Z <= 10**5
        assert D in ('E', 'N')
        assert (X,Y) not in position
        position.add((X, Y))

    assert len(position) == N
    return 0

def main():
    T = int(input())
    assert 1 <= T <= 100
    for _ in range(T):
        N, K = map(int, input().split())
        drones = []
        for _ in range(N):
            X, Y, Z, D = input().split()
            drones.append((int(X), int(Y), int(Z), D))
        solve(N, K, drones)


if __name__ == '__main__':
    main()