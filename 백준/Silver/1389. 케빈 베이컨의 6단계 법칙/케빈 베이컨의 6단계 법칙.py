import sys

n, m = map(int, sys.stdin.readline().split())
lis = [[float('inf') for q in range(n)] for w in range(n)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    lis[a - 1][b - 1] = 1
    lis[b - 1][a - 1] = 1

for i in range(len(lis)):
    lis[i][i] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if lis[j][k] > lis[j][i] + lis[i][k] and j != k and j != i and i != k:
                lis[j][k] = lis[j][i] + lis[i][k]

temp = sorted(lis, key=lambda x: (sum(x), lis.index(x)))
print(lis.index(temp[0]) + 1)