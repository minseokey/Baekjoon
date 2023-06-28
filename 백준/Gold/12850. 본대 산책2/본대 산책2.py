import copy
import math
import sys

fois = int(sys.stdin.readline())
n = 8
lis = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 1, 0],
]
templis = copy.deepcopy(lis)


dplis = []
dplis.append(lis)


def recur(a,b):
    newlis = [[0 for i in range(n)] for j in range(n)]
    for r in range(n):
        for c in range(n):
            temp = 0
            for k in range(n):
                temp += (a[k][c] * b[r][k])
            if temp >= 1000000007:
                newlis[r][c] = temp % 1000000007
            else:
                newlis[r][c] = temp
    return newlis

ans = 0


for i in range(1,int(math.log2(fois)) + 1):
    templis = recur(templis,templis)
    dplis.append(templis)


ske = dplis[0] if fois % 2 == 1 else dplis[1]
for i in range(len(dplis)-1,-1,-1):
    if 2**i < fois:
        fois -= 2**i
        ske = recur(ske,dplis[i])
        if fois <= 2:
            break
ans = ske[0][0]

print(ans % 1000000007)
