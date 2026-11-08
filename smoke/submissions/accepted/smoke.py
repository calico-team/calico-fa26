def solve(N, R, A):
    charges = 2
    cooldown = R
    times = set(A)

    for t in range(A[-1] + 1):
        if charges == 2:
            cooldown = R
        else:
            cooldown -= 1
            if cooldown == 0:
                cooldown = R
                charges += 1

        if t in times:
            if charges:
                charges -= 1
            else:
                return "NO"

    return "YES"

        

T = int(input())
for _ in range(T):
    N, R = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    print(solve(N, R, A))