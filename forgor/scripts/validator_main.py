def solve_phase1(N: int, P: list[int]) -> list[int]:
    assert N == len(P)
    return [0] * N


def main():
    T, phase = map(int, input().split())
    assert T <= 100
    assert phase in [1, 2]
    for _ in range(T):
        N = int(input())
        if phase == 1:
            P = list(map(int, input().split()))
            A = solve_phase1(N, P)


if __name__ == '__main__':
    main()
