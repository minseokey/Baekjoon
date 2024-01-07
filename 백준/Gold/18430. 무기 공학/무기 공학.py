import sys

# form1 -> ㄱ ,form2 ->rㄴ ,form3 -> ㄴ ,form4 -> rㄱ
n, m = map(int, sys.stdin.readline().split())
wood = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
maxz = 0


def form(y, x, f):
    if f == 1 and x > 0 and y < n - 1 and not visited[y][x] and not visited[y][x - 1] and not visited[y + 1][x]:
        visited[y][x], visited[y][x - 1], visited[y + 1][x] = True, True, True
        return wood[y][x] * 2 + wood[y][x - 1] + wood[y + 1][x]
    elif f == 2 and y > 0 and x > 0 and not visited[y][x] and not visited[y][x - 1] and not visited[y - 1][x]:
        visited[y][x], visited[y][x - 1], visited[y - 1][x] = True, True, True
        return wood[y][x] * 2 + wood[y - 1][x] + wood[y][x - 1]
    elif f == 3 and y > 0 and x < m - 1 and not visited[y][x] and not visited[y][x + 1] and not visited[y - 1][x]:
        visited[y][x], visited[y][x + 1], visited[y - 1][x] = True, True, True
        return wood[y][x] * 2 + wood[y - 1][x] + wood[y][x + 1]
    elif f == 4 and y < n - 1 and x < m - 1 and not visited[y][x] and not visited[y][x + 1] and not visited[y + 1][x]:
        visited[y][x], visited[y][x + 1], visited[y + 1][x] = True, True, True
        return wood[y][x] * 2 + wood[y + 1][x] + wood[y][x + 1]
    else:
        return False


def reform(y, x, f):
    if f == 1:
        visited[y][x], visited[y][x - 1], visited[y + 1][x] = False, False, False
    elif f == 2:
        visited[y][x], visited[y][x - 1], visited[y - 1][x] = False, False, False
    elif f == 3:
        visited[y][x], visited[y][x + 1], visited[y - 1][x] = False, False, False
    elif f == 4:
        visited[y][x], visited[y][x + 1], visited[y + 1][x] = False, False, False


def backtrack(y, x, amount):
    global maxz
    if amount > maxz:
        maxz = amount

    for i in range(y,n):
        for j in range(m):
            if not visited[i][j]:
                for f in range(1, 5):
                    am = form(i, j, f)
                    if am:
                        backtrack(i, j, amount + am)
                        reform(i, j, f)


backtrack(0, 0, 0)
print(maxz)
