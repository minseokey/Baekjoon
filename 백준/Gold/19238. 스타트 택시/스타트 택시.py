import sys
from collections import deque

n, m, fuel = map(int, sys.stdin.readline().split())
field = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nowy, nowx = map(int, sys.stdin.readline().split())
nowy -= 1
nowx -= 1
client = dict()
for i in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    client[(a, b)] = (c, d)

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


# BFS
def short(y, x):
    queue = deque([(y, x, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    temp = []
    while queue:
        ty, tx, tc = queue.popleft()
        if (ty, tx) in client.keys():
            temp.append((tc, ty, tx))
        else:
            for dy, dx in DIR:
                if 0 <= ty + dy < n and 0 <= tx + dx < n and not visited[ty + dy][tx + dx] and field[ty + dy][tx + dx] == 0:
                    visited[ty + dy][tx + dx] = True
                    queue.append((ty + dy, tx + dx, tc + 1))

    if temp:
        temp.sort() # c가 가장 작은 기준
        return temp[0][1], temp[0][2], client[(temp[0][1], temp[0][2])][0], client[(temp[0][1], temp[0][2])][1], temp[0][0]
    else:
        return False


# BFS
def app(sty, stx, eny, enx):
    queue = deque([(sty, stx, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[sty][stx] = True
    while queue:
        ty, tx, tc = queue.popleft()
        if ty == eny and tx == enx:
            return tc
        else:
            for dy, dx in DIR:
                if 0 <= ty + dy < n and 0 <= tx + dx < n and not visited[ty + dy][tx + dx] and field[ty + dy][tx + dx] == 0:
                    visited[ty + dy][tx + dx] = True
                    queue.append((ty + dy, tx + dx, tc + 1))

    return False


key = True
while client and key:
    tt = short(nowy, nowx)
    if tt:
        st_y, st_x, en_y, en_x, amount = tt
        client.pop((st_y, st_x))
        # 일단 승객한테 도착
        if fuel >= amount:
            fuel -= amount
            # 만약 도착하면 연료 더해주기, now 위치 변경
            temp = app(st_y, st_x, en_y, en_x)
            if temp and temp <= fuel:
                fuel += temp
                nowy = en_y
                nowx = en_x
            else:
                key = False
                break
        else:
            key = False
            break
    else:
        key = False
        break

# 정상도착
if key:
    print(fuel)
else:
    print(-1)
