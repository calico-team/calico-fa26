def solve(S: str) -> int:
    """
    Return the sum of A and B.
    
    A: a non-negative integer
    B: another non-negative integer
    """
    assert len(S) <= 100
    return 0


def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        S = input()
        solve(S)

if __name__ == '__main__':
    main()
