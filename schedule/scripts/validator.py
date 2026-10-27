def solve(N: int, M: int, K: int, P: list[int]) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    assert 1 <= N <= 10000
    assert 1 <= M <= 50000
    assert 1 <= K <= N
    for x in P:
        assert 0 <= x <= N
    return 0


def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        temp = input().split()
        A, B = int(temp[0]), int(temp[1])
        N, M, K = list(map(int, temp))
        P = list(map(int, input().split()))

if __name__ == '__main__':
    main()
