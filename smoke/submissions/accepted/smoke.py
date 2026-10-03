from collections import deque

t = int(input())
while t:
    temp = input().split(' ')
    r = int(temp[0])
    n = int(temp[1])
    x = list(map(int, input().split()))
    x.sort()

    dq = deque([0, 0])
    works = True

    for y in x:
        z = dq.popleft()
        if z <= y:
            dq.append(y + r)
        else:
            works = False

    print("YES" if works else "NO")
    t -= 1