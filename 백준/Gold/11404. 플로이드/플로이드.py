import sys

node = int(sys.stdin.readline())
vertex = int(sys.stdin.readline())

lis = [[0 for i in range(node)] for j in range(node)]
for i in range(vertex):
    s, d, w = map(int, sys.stdin.readline().split())
    if lis[s - 1][d - 1] == 0:
        lis[s - 1][d - 1] = w
    else:
        lis[s - 1][d - 1] = min(w, lis[s - 1][d - 1])


for i in range(node):
    for j in range(node):
        for k in range(node):
            if lis[j][i] != 0 and lis[i][k] != 0 and j != k:
                if lis[j][k] == 0:
                    lis[j][k] = lis[j][i] + lis[i][k]
                else:
                    lis [j][k] = min(lis[j][i] + lis[i][k], lis[j][k])
for i in lis:
    print(*i)
