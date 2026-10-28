def solve(N: int, A: list[int], V: list[int]):
    assert N <= 200000
    assert len(A) == N
    assert len(V) == N
    for i in range(N):
        assert 1 <= A[i] <= N
        assert 0 <= V[i] < (1 << 30)

def main():
    T = int(input())
    assert T <= 100
    smN = 0
    for _ in range(T):
        N = int(input())
        smN += N
        A = list(map(int, input().split()))
        V = list(map(int, input().split()))
        solve(N, A, V)
    assert smN <= 200000

if __name__ == '__main__':
    main()
