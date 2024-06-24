import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
dic = [[[] for _ in range(n+1)] for _ in range(n+1)]
DIR = [(0,1), (0,-1), (1,0), (-1,0)]
for _ in range(m):
    y, x, a, b = map(int, sys.stdin.readline().split())
    dic[y][x].append((a, b))

wait = [[False] * (n+1) for _ in range(n+1)]
light = [[False] * (n+1) for _ in range(n+1)]
visited = [[False] * (n+1) for _ in range(n+1)]

light[1][1] = True
visited[1][1] = True

queue = deque([(1, 1)])
ans = 1

while queue:
    ty, tx = queue.pop()

    for ny, nx in dic[ty][tx]:
        if not light[ny][nx]:
            light[ny][nx] = True
            ans += 1
            if wait[ny][nx]:
                queue.append((ny, nx))

    for dy, dx in DIR:
        if 0 < ty+dy <= n and 0 < tx+dx <= n and not visited[ty+dy][tx+dx]:
            if light[ty+dy][tx+dx]:
                queue.append((ty+dy, tx+dx))
            else:
                wait[ty+dy][tx+dx] = True
            visited[ty + dy][tx + dx] = True

print(ans)
