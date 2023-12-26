import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
lis = [list(sys.stdin.readline().strip()) for _ in range(r)]
n = int(sys.stdin.readline())
turns = list(map(int, sys.stdin.readline().split()))
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def make_cluster(start):
    queue = deque([start])
    visited = [[False] * c for _ in range(r)]
    visited[start[0]][start[1]] = True
    clus = dict()
    clus[start[1]] = [start[0]]
    bottomkey = False
    while queue:
        ty, tx = queue.popleft()
        for iy, ix in DIR:
            if (0 <= ty + iy < r and 0 <= tx + ix < c and
                    not visited[ty + iy][tx + ix] and lis[ty + iy][tx + ix] == 'x'):
                if ty + iy == r - 1:
                    bottomkey = True
                queue.append((ty + iy, tx + ix))
                if tx+ix in clus.keys():
                    clus[tx+ix].append(ty + iy)
                else:
                    clus[tx+ix] = [ty + iy]
                visited[ty + iy][tx + ix] = True

    if bottomkey:
        return False
    return clus


def move_cluster(clus):
    key = False
    while True:
        newclus = dict()
        for x in clus.keys():
            for y in clus[x]:
                if y+1 < r and lis[y+1][x] == "." or y+1 in clus[x]:
                    if x in newclus.keys():
                        newclus[x].append(y+1)
                    else:
                        newclus[x] = [y+1]
                else:
                    key = True
                    break
            if key:
                break
        if key:
            break

        for x in clus.keys():
            for y in clus[x]:
                lis[y][x] = "."

        for x in newclus.keys():
            for y in newclus[x]:
                lis[y][x] = "x"

        clus = newclus

for ind, height in enumerate(turns):
    height = r - height
    if ind % 2 == 0:
        for i in range(c):
            if lis[height][i] == "x":
                lis[height][i] = "."
                for dy, dx in DIR:
                    if 0 <= height + dy < r and 0 <= i + dx < c and lis[height + dy][i + dx] == "x":
                        temp = make_cluster((height + dy, i + dx))
                        if temp:
                            move_cluster(temp)
                break
    else:
        for i in range(c - 1, -1, -1):
            if lis[height][i] == "x":
                lis[height][i] = "."
                for dy, dx in DIR:
                    if 0 <= height + dy < r and 0 <= i + dx < c and lis[height + dy][i + dx] == "x":
                        temp = make_cluster((height + dy, i + dx))
                        if temp:
                            move_cluster(temp)
                break
for k in lis:
    print("".join(k))

