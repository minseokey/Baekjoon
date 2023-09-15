import sys

n, m, y, x, k = map(int, sys.stdin.readline().split())
maplis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
movelis = list(map(int, sys.stdin.readline().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

ceil = 6
floor = 1
north = 2
south = 5
west = 4
east = 3

#   2
# 4 - 3    ceil = 6, floor = 1
#   5
def flooring(y, x, i):
    global floor,east,west,north,south,ceil
    # 지금 바닥면과 이동 방향을 알때 다음 바닥면은 무었일까?
    if i == 1:
        temp = floor
        floor = east
        east = ceil
        ceil = west
        west = temp

    elif i == 2:
        temp = floor
        floor = west
        west = ceil
        ceil = east
        east = temp

    elif i == 3:
        temp = floor
        floor = north
        north = ceil
        ceil = south
        south = temp

    elif i == 4:
        temp = floor
        floor = south
        south = ceil
        ceil = north
        north = temp


    if maplis[y][x] == 0:
        maplis[y][x] = dice[floor]
    else:
        dice[floor] = maplis[y][x]
        maplis[y][x] = 0

    print(dice[7 - floor])


for i in movelis:
    # 동쪽
    if i == 1 and x < m - 1:
        x += 1
        flooring(y, x, i)
    # 서쪽
    elif i == 2 and 0 < x:
        x -= 1
        flooring(y, x, i)
    # 북쪽
    elif i == 3 and 0 < y:
        y -= 1
        flooring(y, x, i)
    # 남쪽
    elif i == 4 and y < n - 1:
        y += 1
        flooring(y, x, i)
