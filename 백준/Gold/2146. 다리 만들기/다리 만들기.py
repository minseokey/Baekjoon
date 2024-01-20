import sys
from collections import deque

num = int(sys.stdin.readline())

lis = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
visited = [[False] * num for _ in range(num)]
DIR = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def findis(y, x):
    islanslis = []
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    while queue:
        ty, tx = queue.pop()
        islast = False
        for dy, dx in DIR:
            if 0 <= ty + dy < num and 0 <= tx + dx < num:
                if not visited[ty + dy][tx + dx] and lis[ty + dy][tx + dx] == 1:
                    queue.append((ty + dy, tx + dx))
                    visited[ty + dy][tx + dx] = True
                elif lis[ty + dy][tx + dx] == 0:
                    islast = True
        if islast:
            islanslis.append((ty, tx))

    return islanslis


def iml(first, second):
    first = island[first]
    second = island[second]
    minn = float('inf')
    for i in first:
        for j in second:
            minn = min(minn, abs(i[0] - j[0]) + abs(i[1] - j[1]))

    return minn


island = []
for i in range(num):
    for j in range(num):
        if lis[i][j] == 1 and not visited[i][j]:
            island.append(findis(i, j))

# 가장 가까운섬 찾아보자
minlength = float('inf')
for i in range(len(island)):
    for j in range(i + 1, len(island)):
        minlength = min(minlength, iml(i, j))

print(minlength - 1)