from collections import deque

t = int(input())
while t:

    n = int(input())
    x = list(map(int, input().split()))
    x.sort()

    dq = deque([0, 0])
    works = True

    for y in x:
        z = dq.popleft()
        if z <= y:
            dq.append(y + 40)
        else:
            works = False

    print("YES" if works else "NO")
    t -= 1