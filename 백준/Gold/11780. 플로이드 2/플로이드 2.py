import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

INF = float('inf')
lis = [[[INF,[]] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    lis[s - 1][e - 1][0] = min(w, lis[s - 1][e - 1][0])

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k and lis[i][j][0] > lis[i][k][0] + lis[k][j][0]:
                lis[i][j][0] = lis[i][k][0] + lis[k][j][0]
                lis[i][j][1] = lis[i][k][1] + [k+1] + lis[k][j][1]

nlis = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if lis[i][j][0] != INF:
            nlis[i][j] = lis[i][j][0]

for i in nlis:
    print(*i)

for i in range(n):
    for j in range(n):
        if lis[i][j][0] != INF:
            print(len(lis[i][j][1]) + 2, i+1, *lis[i][j][1], j+1)
        else:
            print(0)