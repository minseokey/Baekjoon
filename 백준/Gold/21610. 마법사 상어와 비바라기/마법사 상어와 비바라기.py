import sys

n, m = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
move = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
DIR = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def movecloud(d, s):
    newcloud = []
    for i in range(len(cloud)):
        ty = (cloud[i][0] + (DIR[d][0] * s)) % n
        tx = (cloud[i][1] + (DIR[d][1] * s)) % n
        field[ty][tx] += 1
        newcloud.append((ty,tx))
    return newcloud

def waterbug():
    for y, x in cloud:
        if 0 <= y + 1 < n and 0 <= x+1 < n and field[y+1][x+1] > 0:
            field[y][x] += 1
        if 0 <= y-1 < n and 0 <= x + 1 < n and field[y-1][x+1] > 0:
            field[y][x] += 1
        if 0 <= y - 1 < n and 0 <= x-1 < n and field[y-1][x-1] > 0:
            field[y][x] += 1
        if 0 <= y+1 < n and 0 <= x - 1 < n and field[y+1][x-1] > 0:
            field[y][x] += 1


def updatecloud():
    temp = []
    for y in range(n):
        for x in range(n):
            if field[y][x] >= 2 and (y, x) not in cloud:
                temp.append([y, x])
                field[y][x] -= 2

    return temp

# 각 이동별로
for d, s in move:

    # 구름의 이동
    cloud = movecloud(d - 1, s)

    # 물복사 버그
    waterbug()

    # 새로운 구름 만들기
    cloud = updatecloud()

ans = 0
for y in range(n):
    for x in range(n):
        ans += field[y][x]

print(ans)
