# Source: https://usaco.guide/general/io

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    east = {}
    north = {}
    total = k * n

    for i in range(n):
        x, y, z, direction = input().split()
        x, y = int(x), int(y)
        if (direction == "E"):
            if (x+y not in east):
                east[x + y] = []
            east[x + y].append((x , y))
        else:
            if (x + y not in north):
                north[x + y] = []
            north[x + y].append((x , y))
    for i in east:
        if i in north:
            E = sorted(x for x, y in east[i])
            N = sorted(x for x, y in north[i])
            left = 0
            right = 0

            for nx in N:
                while right < len(E) and E[right] < nx:
                    right += 1
                    
                while left < right and E[left] <= nx - k:
                    left += 1

                total -= right - left
    print(total)
    