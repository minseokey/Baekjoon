import copy
import sys

y, x = map(int, sys.stdin.readline().split())
maze = []

fireQueue = []
jihunQueue = []
jihunVisited = [[False for _ in range(x)] for _ in range(y)]
DIRECRION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(y):
    temp = list(sys.stdin.readline().strip())
    for j in range(x):
        if "J" == temp[j]:
            jihunQueue.append((i, j))
            jihunVisited[i][j] = True
            temp[j] = "."
        if "F" == temp[j]:
            fireQueue.append((i, j))
    maze.append(temp)

key = False
imp = False
count = 0
while not key:
    count += 1
    tempfire = []
    while fireQueue:
        fy,fx = fireQueue.pop()
        for ky, kx in DIRECRION:
            if (y - 1 >= ky + fy >= 0 and x - 1 >= kx + fx >= 0) and maze[ky + fy][kx + fx] == ".":
                maze[ky+fy][kx+fx] = "F"
                tempfire.append((ky+fy, kx+fx))
    fireQueue = copy.deepcopy(tempfire)

    tempjihun = []
    while jihunQueue:
        jy, jx = jihunQueue.pop()
        if jy in [0, y-1] or jx in [0, x-1]:
            key = True
        for ky, kx in DIRECRION:
            if (y - 1 >= ky + jy >= 0 and x - 1 >= kx + jx >= 0) and maze[ky + jy][kx + jx] == ".":
                if not jihunVisited[ky+jy][kx+jx]:
                    tempjihun.append((ky+jy, kx+jx))
                    jihunVisited[ky+jy][kx+jx] = True
    jihunQueue = copy.deepcopy(tempjihun)

    # 마지막 조건
    if not jihunQueue and not key:
        key = True
        imp = True

if imp:
    print("IMPOSSIBLE")
else:
    print(count)