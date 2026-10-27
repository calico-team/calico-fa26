def submit(GUESS: str) -> str:
    """
    Send one guess to the judge and return the judge's reply.

    GUESS: a string of length N, one character per position
    Returns: the judge's reply for this guess: either the string
             "CORRECT", or a string of length N where position i shows
             the true character if GUESS[i] was correct and "_" otherwise.
    """
    print(GUESS, flush=True)
    return input()


def solve(N: int, K: int, A: list[str]) -> None:
    """
    Guess the hidden string of length N.

    N: the length of the hidden string
    K: the number of allowed characters
    A: the list of the K allowed characters
    The hidden string must be guessed using submit(); use no more than
    2*N guesses.
    """
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
