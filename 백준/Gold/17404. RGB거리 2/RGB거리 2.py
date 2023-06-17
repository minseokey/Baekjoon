import copy
import sys

n = int(input())
ans = 0
lis = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
INF = float('inf')
lisst0 = [lis[0][0], INF, INF]
lisst1 = [INF, lis[0][1], INF]
lisst2 = [INF, INF, lis[0][2]]

lis0 = copy.deepcopy(lis)
lis0[0] = lisst0
lis1 = copy.deepcopy(lis)
lis1[0] = lisst1
lis2 = copy.deepcopy(lis)
lis2[0] = lisst2

def recur(i,lis):
    lis[i+1][0] += min(lis[i][1],lis[i][2])
    lis[i+1][1] += min(lis[i][0],lis[i][2])
    lis[i+1][2] += min(lis[i][0],lis[i][1])

for i in range(n-1):
    recur(i,lis0)
    recur(i,lis1)
    recur(i,lis2)

lis0[-1][0] = INF
lis1[-1][1] = INF
lis2[-1][2] = INF
print(min(*lis0[-1],*lis1[-1],*lis2[-1]))