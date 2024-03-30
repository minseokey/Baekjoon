import copy
import sys

n, m, t = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
rot = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

for x, d, k in rot:
    # x의 배수를 d방향으로 k만큼
    for mx in range(x, n + 1, x):
        mx -= 1
        # 시계방향
        if d == 0:
            temp = lis[mx][m - k:]
            lis[mx] = temp + lis[mx][:m - k]
        # 반시계방향
        else:
            temp = lis[mx][:k]
            lis[mx] = lis[mx][k:] + temp


    key = False
    tlis = copy.deepcopy(lis)
    # 같은수가 있나 확인
    for i in range(n):
        for j in range(m):
            if tlis[i][j] != 0:
                if j != m - 1:
                    if tlis[i][j] == tlis[i][j + 1]:
                        lis[i][j] = 0
                        lis[i][j+1] = 0
                        key = True
                else:
                    if tlis[i][j] == tlis[i][0]:
                        lis[i][j] = 0
                        lis[i][0] = 0
                        key = True


                if i != n - 1:
                    if tlis[i][j] == tlis[i + 1][j]:
                        lis[i][j] = 0
                        lis[i+1][j] = 0
                        key = True

    # 평균보고 +- 1
    if not key:
        tt = 0
        su = 0
        for yy in lis:
            for xx in yy:
                if xx != 0:
                    su += xx
                    tt += 1
        if tt > 0:
            md = su / tt
            for mx in range(n):
                for mmx in range(m):
                    if lis[mx][mmx] > md:
                        lis[mx][mmx] -= 1
                    elif lis[mx][mmx] < md and lis[mx][mmx] != 0:
                        lis[mx][mmx] += 1


print(sum(map(sum, lis)))
