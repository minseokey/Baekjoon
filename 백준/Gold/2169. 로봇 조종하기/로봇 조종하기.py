import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
lis = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 첫줄 -> only 좌로이동
for i in range(1,m):
    lis[0][i] += lis[0][i-1]

# 여기있는 lis 를 가지고 좌로 최대값, 우로 최대값 찾기

for i in range(1, n):
    # 좌로최대
    dpleft = copy.deepcopy(lis[i])
    # 우로최대
    dpright = copy.deepcopy(lis[i])

    for k in range(m):
        if k == 0:
            dpleft[0] += lis[i-1][0]
        else:
            dpleft[k] += max(lis[i - 1][k], dpleft[k - 1])
    for k in range(m-1, -1, -1):
        if k == m-1:
            dpright[m-1] += lis[i-1][m-1]
        else:
            dpright[k] += max(lis[i - 1][k], dpright[k + 1])

    for k in range(m):
        lis[i][k] = max(dpleft[k], dpright[k])


print(lis[-1][-1])