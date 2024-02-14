import sys

m, n = map(int, sys.stdin.readline().split())
beewax = [[1] * m for _ in range(m)]

# 3 -> [0,2],[0,1],[0,0],[1,0],[2,0]

ADDLIS = []
for i in range(m - 1, 0, -1):
    ADDLIS.append((i, 0))
for i in range(m):
    ADDLIS.append((0, i))


for _ in range(n):
    groth = list(map(int, sys.stdin.readline().split()))  # 0개수 1개수 2개수
    A_ind = 0
    A_ind += groth[0]
    beeG = [[0] * m for _ in range(m)]

    for i in range(groth[1]):
        beewax[ADDLIS[A_ind][0]][ADDLIS[A_ind][1]] += 1
        beeG[ADDLIS[A_ind][0]][ADDLIS[A_ind][1]] = 1
        A_ind += 1
    for i in range(groth[2]):
        beewax[ADDLIS[A_ind][0]][ADDLIS[A_ind][1]] += 2
        beeG[ADDLIS[A_ind][0]][ADDLIS[A_ind][1]] = 2
        A_ind += 1

    # 여기까지 작업 끝.
    for i in range(1,m):
        for j in range(1,m):
            temp = max(beeG[i-1][j], beeG[i-1][j-1], beeG[i][j-1])
            beeG[i][j] = temp
            beewax[i][j] += temp


for i in beewax:
    print(*i)