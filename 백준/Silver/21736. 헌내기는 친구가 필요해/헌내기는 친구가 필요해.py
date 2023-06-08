import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())
doyeon = []
visited = [[False for _ in range(x)] for _ in range(y)]
lis = [list(sys.stdin.readline().strip()) for _ in range(y)]
key = False

for i in range(y):
    for j in range(x):
        if lis[i][j] == "I":
            doyeon = [i,j]
            key = True
            break
    if key:
        break

DEST = [[0, 1], [1, 0], [0, -1], [-1, 0]]
queue = deque()
queue.append(doyeon)

count = 0
while queue:
    ty, tx = queue.popleft()
    for dy, dx in DEST:
        if 0 <= tx + dx < x and 0 <= ty + dy < y:
            if lis[ty + dy][tx + dx] != "X" and not visited[ty + dy][tx + dx]:
                visited[ty + dy][tx + dx] = True
                queue.append([ty + dy, tx + dx])
                if lis[ty + dy][tx + dx] == "P":
                    count += 1

if count != 0:
    print(count)
else:
    print("TT")
