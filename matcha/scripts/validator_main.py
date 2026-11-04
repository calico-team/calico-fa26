def solve(N: int, L: list[int], R: list[int]):
    assert N <= 200000
    assert len(L) == N 
    assert len(R) == N 
    for i in range(N):
        assert 0 <= L[i] <= R[i] < (1 << 30)

def main():
    T = int(input())
    assert 1 <= T <= 100000
    smN = 0
    for _ in range(T):
        N = int(input())
        smN += N
        L = list(map(int, input().split()))
        R = list(map(int, input().split()))
        solve(N, L, R)
    assert 1 <= smN <= 200000

if __name__ == '__main__':
    main()
