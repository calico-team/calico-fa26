"""
* N: Number of drones
* K: Number of nights
* drone: a list in this order [x_coordinate, y_coordinate, z_coordinate, direction] for each drone
"""


def solve(N: int, K: int, drones: list):
    answer = 0
    return answer

def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        drones = []
        for _ in range(n):
            x, y, z, d = input().split()
            drones.append((int(x), int(y), int(z), d))

        print(solve(n, k, drones))


if __name__ == '__main__':
    main()