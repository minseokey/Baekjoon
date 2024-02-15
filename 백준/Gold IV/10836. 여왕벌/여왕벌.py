import sys

m, n = map(int, sys.stdin.readline().split())
beewax = [[1] *m for _ in range(m)]

Ay = []
Ax = []
for i in range(m - 1, 0, -1):
    Ay.append(i)
    Ax.append(0)
for i in range(m):
    Ay.append(0)
    Ax.append(i)

# 유일한 이중루프
for _ in range(n):
    z,o,t = list(map(int, sys.stdin.readline().split()))  # 0개수 1개수 2개수

    for i in range(z, z+o):
        beewax[Ay[i]][Ax[i]] += 1
    for i in range(z+o, z+o+t):
        beewax[Ay[i]][Ax[i]] += 2

for i in range(1, m):
    for j in range(1, m):
        beewax[j][i] = beewax[0][i]

for j in beewax:
    print(*j)

