def solve(N: int, R: int, A: list[int]) -> str:
    """
    Return whether Omen can throw a smoke for every teammate request.

    N: the number of requests
    R: the number of seconds it takes for a smoke to recharge
    A: the times (in seconds) at which each request is made
    """
    # YOUR CODE HERE
    return ""


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        N = int(temp[0])
        R = int(temp[1])
        A = list(map(int, input().split()))
        print(solve(N, R, A))


if __name__ == '__main__':
    main()
