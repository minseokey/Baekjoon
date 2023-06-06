import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())
lis = []
start = []
for i in range(y):
    temp = list(map(int, sys.stdin.readline().split()))
    if 2 in temp:
        start = [i, temp.index(2)]
    lis.append(temp)

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque()
start.append(1)
queue.append(start)
visited = [[False for _ in range(x)] for _ in range(y)]
lis[start[0]][start[1]] = 0
visited[start[0]][start[1]] = True

while queue:
    ty, tx, cnt = queue.popleft()
    for dy, dx in dir:
        if 0 <= ty + dy < y and 0 <= tx + dx < x:
            if not visited[ty + dy][tx + dx] and lis[ty + dy][tx + dx] != 0:
                visited[ty + dy][tx + dx] = True
                queue.append([ty + dy, tx + dx, cnt + 1])
                lis[ty + dy][tx + dx] = cnt

for i in range(y):
    for j in range(x):
        if lis[i][j] == 1 and visited[i][j] == False:
            lis[i][j] = -1
for i in lis:
    print(*i)
