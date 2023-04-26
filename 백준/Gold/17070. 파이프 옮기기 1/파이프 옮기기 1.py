import sys
from collections import deque

n = int(sys.stdin.readline())
lis = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dplist = [[[0, 0, 0] for a in range(n)] for b in range(n)]
dplist[0][1][0] = 1
# 0 가로, 1 세로, 2 대각
for i in range(n):  # y
    for j in range(n):  # x
        if j < n - 1 and lis[i][j + 1] != 1:
            dplist[i][j + 1][0] += dplist[i][j][0] + dplist[i][j][2]
        if i < n - 1 and lis[i + 1][j] != 1:
            dplist[i + 1][j][1] += dplist[i][j][1] + dplist[i][j][2]
        if j < n - 1 and i < n - 1 and lis[i][j + 1] != 1 and lis[i + 1][j] != 1 and lis[i + 1][j + 1] != 1:
            dplist[i + 1][j + 1][2] += dplist[i][j][0] + dplist[i][j][1] + dplist[i][j][2]

print(sum(dplist[-1][-1]))