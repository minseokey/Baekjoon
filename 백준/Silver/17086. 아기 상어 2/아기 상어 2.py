import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1), (1,1),(1,-1),(-1,1),(-1,-1)]
num = 0


def findlength(y, x):
    queue = deque([(y, x, 0)])
    temp = float('inf')
    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True

    while queue:
        ty, tx, cnt = queue.popleft()
        if field[ty][tx] == 1:
            temp = min(temp, cnt)
            break
        elif cnt < temp:
            for dy, dx in DIR:
                if 0 <= ty + dy < n and 0 <= tx + dx < m and not visited[ty+dy][tx+dx]:
                    queue.append((ty + dy, tx + dx, cnt + 1))
                    visited[ty+dy][tx+dx] = True

    return temp


for i in range(n):
    for j in range(m):
        if field[i][j] == 0:
            num = max(num, findlength(i, j))

print(num)
