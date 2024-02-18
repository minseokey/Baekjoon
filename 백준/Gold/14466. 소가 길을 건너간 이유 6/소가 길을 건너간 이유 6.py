import sys
from collections import defaultdict
import copy

n, k, r = map(int, sys.stdin.readline().split())

banned = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r):
    a, b, aa, bb = map(int, sys.stdin.readline().split())
    banned[a][b].append([aa, bb])
    banned[aa][bb].append([a, b])

cow = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(pos):
    y, x = pos[0], pos[1]
    # bfs로 도착이 가능한지 파악하자.
    field = [[False] * (n + 1) for _ in range(n + 1)]
    stack = [(y, x)]
    while stack:
        ty, tx = stack.pop()
        for dy, dx in DIR:
            if 0 < ty + dy <= n and 0 < tx + dx <= n and not field[ty + dy][tx + dx] and [ty+dy,tx+dx] not in banned[ty][tx]:
                    field[ty + dy][tx + dx] = True
                    stack.append((ty + dy, tx + dx))
    return field


ans = 0
for i in range(len(cow)):
    temp = bfs(cow[i])
    for j in range(i + 1, len(cow)):
        if not temp[cow[j][0]][cow[j][1]]:
            ans += 1

print(ans)
