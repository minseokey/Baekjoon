import sys

n = int(sys.stdin.readline())
visitedlis = [[False for _ in range(2 * n - 1)] for _ in range(2 * n - 1)]
originlis = [list(sys.stdin.readline().split()) for _ in range(n)]

ans = 0


def recur(y, x, count):
    global ans
    # 짝수
    if n % 2 == 0:
        if x == n + 1:
            x = 0
            y += 1
        elif x == n:
            x = 1
            y += 1
    # 홀수
    elif n % 2 == 1:
        if x == n + 1:
            x = 1
            y += 1
        elif x == n:
            x = 0
            y += 1

    if y == n:
        ans = max(ans,count)
        return
    # 백트래킹
    # 하난 합, 하난 차
    if originlis[y][x] == "1" and not visitedlis[0][x + y] and not visitedlis[1][y - x + n - 1]:
        visitedlis[0][x + y] = True
        visitedlis[1][y - x + n - 1] = True
        recur(y, x + 2, count + 1)
        visitedlis[0][x + y] = False
        visitedlis[1][y - x + n - 1] = False
    recur(y, x + 2, count)


gans = 0
recur(0, 0, 0)
gans += ans
ans = 0
recur(0, 1, 0)
gans += ans
print(gans)
