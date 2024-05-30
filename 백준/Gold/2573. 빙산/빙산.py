import sys
from collections import deque

y, x = map(int, sys.stdin.readline().split())
DIR = [(1, 0), (0, 1), (0, -1), (-1, 0)]
lis = []
dic = dict()
for i in range(y):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(x):
        if temp[j] != 0:
            dic[(i, j)] = temp[j]
    lis.append(temp)


def check_sep():
    # 만약 아무점에서 BFS 돌렸을때, 모든 점을 찍지 못하면 2개로 나누어진거다
    queue = deque()
    visited = set(dic.keys())
    queue.append(list(dic.keys())[0])
    while queue:
        ny, nx = queue.popleft()
        for dy, dx in DIR:
            if lis[dy + ny][dx + nx] != 0 and (ny + dy, nx + dx) in visited:
                queue.append((dy + ny, dx + nx))
                visited.remove((ny + dy, nx + dx))
    # 남아있다면
    if visited:
        return True
    else:
        return False


def melt():
    m_1 = []
    for ty, tx in dic.keys():
        water = 0
        for tdy, tdx in DIR:
            if lis[ty + tdy][tx + tdx] == 0:
                water += 1
        m_1.append((ty, tx, water))

    for ty, tx, water in m_1:
        if lis[ty][tx] >= water:
            lis[ty][tx] -= water
            dic[(ty, tx)] -= water
            if lis[ty][tx] <= 0:
                lis[ty][tx] = 0
                dic.pop((ty, tx))
        else:
            dic.pop((ty, tx))
            lis[ty][tx] = 0


count = 0
key = False
while dic.keys():
    count += 1
    melt()
    if dic.keys():
        if check_sep():
            key = True
            break
    else:
        break

if key:
    print(count)
else:
    print(0)
