def solve(N: int, A: list[int], B: list[int]):
    assert N <= 200000
    assert len(A) == N
    assert len(B) == N
    for i in range(N):
        assert 0 <= A[i] < (1 << 30)
        assert 1 <= B[i] <= N


def main():
    T = int(input())
    assert T <= 100
    smN = 0
    for _ in range(T):
        N = int(input())
        smN += N
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        solve(N, A, B)
    assert smN <= 200000

if __name__ == '__main__':
    main()
