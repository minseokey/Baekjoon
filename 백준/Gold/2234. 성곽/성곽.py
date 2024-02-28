import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
path = [[[True] * 4 for _ in range(m)] for _ in range(n)]
wall = []  # (y,x,index) 형태로 저장.

for i in range(n):
    for j in range(m):
        if lis[i][j] // 8 == 1:
            lis[i][j] %= 8
            path[i][j][3] = False
            if 0 < i < n - 1 and 0 < j < m - 1:
                wall.append((i, j, 3))
        if lis[i][j] // 4 == 1:
            lis[i][j] %= 4
            path[i][j][2] = False
            if 0 < i < n - 1 and 0 < j < m - 1:
                wall.append((i, j, 2))
        if lis[i][j] // 2 == 1:
            lis[i][j] %= 2
            path[i][j][1] = False
            if 0 < i < n - 1 and 0 < j < m - 1:
                wall.append((i, j, 1))
        if lis[i][j] == 1:
            path[i][j][0] = False
            if 0 < i < n - 1 and 0 < j < m - 1:
                wall.append((i, j, 0))

DIR = [(0, -1), (-1, 0), (0, 1), (1, 0)]

visited = [[False] * m for _ in range(n)]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    temp = [(y, x)]
    while queue:
        ty, tx = queue.popleft()
        for ind, d in enumerate(DIR):
            if path[ty][tx][ind] and not visited[ty + d[0]][tx + d[1]]:  # 만약 벽이 없고, 지나갈 수 있다면,
                queue.append((ty + d[0], tx + d[1]))
                visited[ty + d[0]][tx + d[1]] = True
                temp.append((ty + d[0], tx + d[1]))
    return temp


def beside(a, b):
    for i in a:
        for j in b:
            if abs(i[0] - j[0]) + abs(i[1] - j[1]) == 1:  # 한칸차이
                return True
    return False


count = 0
maxx = 0
rooms = []
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            temp = bfs(i, j)
            maxx = max(maxx, len(temp))
            rooms.append(temp)

two_max = 0
for i in range(len(rooms)):
    for j in range(i + 1, len(rooms)):
        # i,j 가 만약 한칸 차이인것이 있을때, 이 두개를 합쳤을때의 합의 최대.
        if beside(rooms[i], rooms[j]):
            two_max = max(two_max, len(rooms[i]) + len(rooms[j]))

print(count)
print(maxx)
print(two_max)
