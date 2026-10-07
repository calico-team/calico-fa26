def solve(M: int, N: int, F: int) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    assert M <= 100
    assert N <= 100
    assert F <= 25
    return 0


def main():
    T = int(input())
    assert T <= 10
    for _ in range(T):
        temp = input().split()
        M, N, F = int(temp[0]), int(temp[1]), int(temp[2])
        grid = [input() for i in range(M)]
        assert len(grid) == M
        for i in grid:
            assert len(i) == N
    


if __name__ == '__main__':
    main()
