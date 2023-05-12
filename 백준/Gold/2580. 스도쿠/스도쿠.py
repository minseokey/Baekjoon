import sys

plate = []
zero = []
for i in range(9):
    plate.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if plate[i][j] == 0:
            zero.append([i, j])


def checkx(a, y):
    for k in range(9):
        if a == plate[y][k]:
            return False
    return True


def checky(a, x):
    for k in range(9):
        if a == plate[k][x]:
            return False
    return True


def checksq(a, x, y):
    x = x // 3 * 3
    y = y // 3 * 3
    for k in range(3):
        for l in range(3):
            if plate[y + k][x + l] == a:
                return False
    return True


def dfs(index):
    if len(zero) == index:
        for q in plate:
            print(*q)
        exit(0)

    # 1 ~ 10 까지의 무한 테스트. 맞으면 stop
    for o in range(1, 10):
        y = zero[index][0]
        x = zero[index][1]
        if checky(o, x) and checkx(o, y) and checksq(o, x, y):
            plate[y][x] = o
            dfs(index + 1)
            # 아닌경우에 빠꾸하는 메커니즘
            plate[y][x] = 0


dfs(0)
