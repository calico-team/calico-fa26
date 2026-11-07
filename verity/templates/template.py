
import sys
from functools import partial

"""
* Print a string that could be the answer string
*
* N: Length of the string
* K: Number of different -ities
* A: List containing the different -ities
"""
print = partial(print, flush=True)

def solve(N: int, K: int, A: list[str]) -> None:
    # YOUR CODE HERE
    pass


def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        A = input().split()

        solve(N, K, A)


if __name__ == '__main__':
    main()
