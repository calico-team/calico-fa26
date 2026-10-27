def solve(N: int, X: list[int], Y: list[int], Z: list[int], DIR: list[str], K: int) -> int:
    """
    Return the total units of rain collected over the K nights.

    N: the number of drones
    X: the starting x coordinate of each drone
    Y: the starting y coordinate of each drone
    Z: the starting z coordinate of each drone
    DIR: the direction of each drone, one of 'N' or 'E'
    K: the number of nights
    """
    # YOUR CODE HERE
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        X = []
        Y = []
        Z = []
        DIR = []
        for _ in range(N):
            x, y, z, d = input().split()
            X.append(int(x))
            Y.append(int(y))
            Z.append(int(z))
            DIR.append(d)
        print(solve(N, X, Y, Z, DIR, K))


if __name__ == '__main__':
    main()
