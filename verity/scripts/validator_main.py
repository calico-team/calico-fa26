def solve(N: int, K: int, A: list[str]):
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """

    assert N <= 100
    assert K <= 26
    assert len(A) == K
    
    return 


def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        temp = input().split()
        N, K = int(temp[0]), int(temp[1])
        A = input().split()

        solve(N, K, A)


if __name__ == '__main__':
    main()