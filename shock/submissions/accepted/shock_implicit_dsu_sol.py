"""
*Return an N by M grid displaying the reading of the block seismometers after all earthquakes occur.
*
*N: number of rows in the grid
*M: number of columns in the grid
*Q: number of earthquakes
*earthquakes: a list of tuples (X, Y, P), where:
*    X: column of the epicenter
*    Y: row of the epicenter
*    P: power of the earthquake
"""
def solve(N, M, Q, earthquakes):
    do_swap = (N > M)
    if do_swap:
        N, M = M, N
    nxt = [[i+1 for i in range(M)] for _ in range(N)]
    ans = [[0] * M for _ in range(N)]
    for ogy, ogx, p in reversed(earthquakes):
        y,x = ogy, ogx
        if do_swap:
            y,x = x,y
        xi = x
        for yi in range(y-p,y+1):
            while (xi-x)**2+(yi-y)**2 <= p*p:
                xi += 1
            xi -= 1
            curx = x-(xi-x)

            to_update = []
            while curx <= xi and ans[yi][curx] != 0:
                curx = nxt[yi][curx]
            while curx <= xi:
                to_update.append(curx)
                ans[yi][curx] = p**2-(yi-y)**2-(curx-x)**2+1
                while curx <= xi and ans[yi][curx] != 0:
                    curx = nxt[yi][curx]
            for xupdate in to_update:
                nxt[yi][xupdate] = curx

            curx = x-(xi-x)
            yc = 2*y-yi
            to_update = []
            while curx <= xi and ans[yc][curx] != 0:
                curx = nxt[yc][curx]
            while curx <= xi:
                to_update.append(curx)
                ans[yc][curx] = p**2-(yc-y)**2-(curx-x)**2+1
                while curx <= xi and ans[yc][curx] != 0:
                    curx = nxt[yc][curx]
            for xupdate in to_update:
                nxt[yc][xupdate] = curx
    if do_swap:
        ans = [[ans[i][j] for i in range(len(ans))] for j in range(len(ans[0]))]
    return ans

def main():
    T = int(input())
    for _ in range(T):
        N, M, Q = map(int, input().split())
        earthquakes = []
        for i in range(Q):
            X, Y, P = map(int, input().split())
            earthquakes.append((X, Y, P))
        answer = solve(N, M, Q, earthquakes)
        for row in answer:
            print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()