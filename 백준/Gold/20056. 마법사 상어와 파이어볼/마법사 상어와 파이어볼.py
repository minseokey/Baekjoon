import sys
n, w, k = map(int, sys.stdin.readline().split())
field = [[[] for _ in range(n)] for _ in range(n)]  # mi,si,di

for i in range(w):
    y, x, m, s, d = map(int, sys.stdin.readline().split())
    field[y-1][x-1].append([m, s, d])

dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def dircheck(dirlis):
    key = []
    for dd in dirlis:
        if dd % 2 == 1 and "e" in key:
            return False
        elif dd % 2 == 0 and "o" in key:
            return False
        elif dd % 2 == 1:
            key.append("o")
        elif dd % 2 == 0:
            key.append("e")
    return True


def gather_fireball(ball_lis, ty, tx):
    # 여러개의 공이 하나의 위치로 왔을때 가정.
    if len(ball_lis) >= 2:
        allm = []
        alls = []
        alld = []
        for tm, ts, td in ball_lis:
            allm.append(tm)
            alls.append(ts)
            alld.append(td)

        newm = sum(allm) // 5
        news = sum(alls) // len(alls)
        if dircheck(alld):
            newd = [0, 2, 4, 6]
        else:
            newd = [1, 3, 5, 7]

        if newm > 0:
            temp = []
            for p in range(4):
                temp.append([newm, news, newd[p]])
            real_temp_field[ty][tx] = temp
    else:
        real_temp_field[ty][tx] = ball_lis


def move_fireball(ball_lis, ky, kx):
    for tm, ts, td in ball_lis:
        ty, tx = ky, kx
        ty += (dir[td][0] * ts)
        tx += (dir[td][1] * ts)
        ty%=n
        tx%=n
        temp_field[ty][tx].append([tm, ts, td])


for i in range(k):
    # 한턴이 돌때. -> 이동후에, 합쳐진다
    temp_field = [[[] for _ in range(n)] for _ in range(n)]
    real_temp_field = [[[] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if field[r][c]:
                move_fireball(field[r][c], r, c)
    for r in range(n):
        for c in range(n):
            if temp_field[r][c]:
                gather_fireball(temp_field[r][c], r, c)
    field = real_temp_field

ans = 0
for i in field:
    for j in i:
        for o in j:
            ans += o[0]

print(ans)
