def solve(N: int, A: list[int], B: list[int]) -> list[int]:
    """
    Return an array of N integers, the i-th of which
    represents Big Ben's maximum happiness if he 
    starts by trying to define word i.

    N: the number of words in the dictionary
    A: the value associated with the happiness of each word
    B: the first word in the definition of word i
    """
    # YOUR CODE HERE 
    return []

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        print(' '.join(map(str, solve(N, A, B))))

if __name__ == '__main__':
    main()
