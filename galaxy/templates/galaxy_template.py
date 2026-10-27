def solve(N: int, M: int, G: list[str]) -> str:
    """
    Return whether Ben can reach the bottom-right tile of the grid.

    N: the number of rows in the grid
    M: the number of columns in the grid
    G: the grid, where G[i] is the i-th row and each character is one of
       'R', 'B', or '.'
    """
    # YOUR CODE HERE
    return ""


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            G.append(input())
        print(solve(N, M, G))


if __name__ == '__main__':
    main()
