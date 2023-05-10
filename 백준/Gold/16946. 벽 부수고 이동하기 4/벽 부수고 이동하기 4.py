import copy
import sys
from collections import deque

y,x = map(int,sys.stdin.readline().split())
waylis = []
walllis = []
alllis = []

n = 0
for i in range(y):
    temp = list(sys.stdin.readline().strip())
    alllis.append(temp)
    for j in range(x):
        if temp[j] == "0":
            waylis.append((i,j))
        if temp[j] == "1":
            walllis.append((i,j))
            n += 1

visit = [[False for i in range(x)] for j in range(y)]
indext = 0
space = dict()
newlis = [['-' for i in range(x)] for j in range(y)]

for i in waylis:
    if not visit[i[0]][i[1]]:
        queue = deque()
        queue.append(i)
        strind = str(indext)
        visit[i[0]][i[1]] = True
        newlis[i[0]][i[1]] = strind
        templis = []
        t = 1
        while queue:
            ty,tx = queue.popleft()

            if ty > 0 and not visit[ty - 1][tx] and alllis[ty - 1][tx] == '0':
                visit[ty - 1][tx] = True
                newlis[ty - 1][tx] = strind
                templis.append((ty - 1,tx))
                queue.append((ty - 1, tx))
                t += 1
            if tx > 0 and not visit[ty][tx - 1] and alllis[ty][tx - 1] == '0':
                visit[ty][tx - 1] = True
                newlis[ty][tx - 1] = strind
                templis.append((ty,tx - 1))
                queue.append((ty, tx - 1))
                t += 1
            if ty < y - 1 and not visit[ty + 1][tx] and alllis[ty + 1][tx] == '0':
                visit[ty + 1][tx] = True
                newlis[ty + 1][tx] = strind
                templis.append((ty + 1,tx))
                queue.append((ty + 1, tx))
                t += 1
            if tx < x - 1 and not visit[ty][tx + 1] and alllis[ty][tx + 1] == '0':
                visit[ty][tx + 1] = True
                newlis[ty][tx + 1] = strind
                templis.append((ty,tx + 1))
                queue.append((ty, tx + 1))
                t += 1

        space[strind] = t
        indext += 1


for ty,tx in walllis:
    tempset = set()
    if ty > 0 and newlis[ty - 1][tx] != '-':
        tempset.add(newlis[ty - 1][tx])
    if tx > 0 and newlis[ty][tx - 1] != '-':
        tempset.add(newlis[ty][tx - 1])
    if ty < y - 1 and newlis[ty + 1][tx] != '-':
        tempset.add(newlis[ty + 1][tx])
    if tx < x - 1 and newlis[ty][tx + 1] != '-':
        tempset.add(newlis[ty][tx + 1])
    ans = 0
    for i in tempset:
        ans += space[i]
    alllis[ty][tx] = str((ans + 1)%10)

for i in alllis:
    print("".join(i))