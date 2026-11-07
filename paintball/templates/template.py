"""
*Output an N by M grid displaying the reading of the block seismometers after all earthquakes occur.
*
*N: number of rows in the grid
*M: number of columns in the grid
*Q: number of earthquakes
*earthquake: a list of tuples (X, Y, P), where:
*    X: column of the epicenter
*    Y: row of the epicenter
*    P: power of the earthquake
"""
def solve(N, M, Q, earthquake):
    pass


def main():
    T = int(input())
    for _ in range(T):
        N, M, Q = map(int, input().split())
        earthquake = []
        for i in range(Q):
            X, Y, P = map(int, input().split())
            earthquake.append((X, Y, P))
        solve(N, M, Q, earthquake)

if __name__ == '__main__':
    main()