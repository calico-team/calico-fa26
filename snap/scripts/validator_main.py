def solve(M: int, N: int, F: int) -> int:
    assert M < 100
    assert N < 100
    assert F < 25
    assert F <= M
    assert F <= N

    return 0



def main():
    T = int(input())
    assert T <= 100
    for _ in range(T):
        temp = input().split()
        M, N, F = int(temp[0]), int(temp[1]), int(temp[2])

if __name__ == '__main__':
    main()
